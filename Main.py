# Lucas Roberts #001085316
# C950 WGUPS Project

from HashTable import HashTable
import csv
import datetime
from Location import Location
from Package import Package
from Truck import Truck

# create hash table for package data
packages = HashTable()

# import CSV data for packages and insert into hash table
# O(N)
with open('WGUPS Package File.csv') as csvfile:
    readPackageCSV = csv.reader(csvfile, delimiter=',')
    for row in readPackageCSV:
        if len(row) == 8:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.insert(package)
        else:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            packages.insert(package)

# Creates dict for locations.
locations = {}

# bring in location data from CSV
# O(N)
with open('WGUPSLocations.csv') as csvfile:
    readPackageCSV = csv.reader(csvfile, delimiter=',')
    for row in readPackageCSV:
        location = Location(row[0], row[1], row[2])
        locations[location.id] = location

# add neighbors and distances to each location
# O(N^2)
with open('WGUPSLocations.csv') as csvfile:
    readPackageCSV = csv.reader(csvfile, delimiter=',')
    rows = list(readPackageCSV)
for k, v in locations.items():
    for i in range(0, 27):
        v.add_neighbor(locations.get(str(i)), rows[i][int(v.id) + 3])

# Associates location to each package.
# O(N^2)
for i in range(1, 41):
    package_to_mark = packages.lookup_item(i)
    for k, v in locations.items():
        if package_to_mark.address in v.address:
            package_to_mark.location = v

# Creates truck objects. The third truck is not used.
truck1 = Truck(1, locations.get(str(0)))
truck2 = Truck(2, locations.get(str(0)))
truck3 = Truck(3, locations.get(str(0)))


# This function is used to run the entire simulation.
def run_simulation(time='all', package_command='all'):
    # First round of adding packages
    # O(N) - N being the number of items in the range.
    for i in range(1, 41):
        package_being_loaded = packages.lookup_item(i)
        if "truck 2" in packages.lookup_item(i).notes:
            truck2.add_package(packages.lookup_item(i))
        elif "Delayed" in packages.lookup_item(i).notes:
            packages.lookup_item(i).status_delayed()
        elif "Wrong" in packages.lookup_item(i).notes:
            packages.lookup_item(i).status_wrong_address()
        elif "Must be" in packages.lookup_item(i).notes or packages.lookup_item(i).package_id in (13, 15, 19):
            truck1.add_package(packages.lookup_item(i))
        elif packages.lookup_item(i).deadline != "EOD":
            truck1.add_package(packages.lookup_item(i))
        elif packages.lookup_item(i).deadline == "EOD":
            truck2.add_package(packages.lookup_item(i))

    # Begins second round of adding packages for Truck 1. Ensures that a package is not meant for truck 2 first.
    # O(N) - N being the number of packages to parse through.
    while truck1.cargo_count != 16:
        for i in range(1, 41):
            if "truck 2" not in packages.lookup_item(i).notes:
                if packages.lookup_item(i).status == "HUB":
                    truck1.add_package(packages.lookup_item(i))

    # Begins second round of adding packages for Truck 2. Will not add package 26 due to deadline constraints.
    # O(N) - N being the number of packages to parse through.
    while truck2.cargo_count != 16:
        for i in range(1, 40):
            if packages.lookup_item(i).status == "HUB" and packages.lookup_item(i).package_id != 26:
                truck2.add_package(packages.lookup_item(i))

    # Associates a package with a location specifically for the truck.
    # O(N)
    for package in truck1.cargo:
        truck1.cargo_addresses[package] = package.location

    # Begins delivery route of the truck.
    # O(N^2) - due to worst case of the .closest_neighbor function inside of the .next_stop function
    while truck1.cargo_count != 0:
        if truck1.time_up:
            break;
        else:
            truck1.next_stop(time)

    # Manually drives the truck to the hub so it can pick up more packages.
    truck1.drive_to(locations.get('0'), time)

    # Begins picking up more packages. Skips over package #25 for time constraints.
    # O(N)
    for i in range(1, 41):
        if "truck 2" not in packages.lookup_item(i).notes:
            if packages.lookup_item(i).status == "HUB":
                truck1.add_package(packages.lookup_item(i))
            elif packages.lookup_item(i).status == "DELAYED" and packages.lookup_item(i).package_id != 25:
                truck1.add_package(packages.lookup_item(i))

    # Associates packages with locations specifically for this truck.
    # O(N)
    for package in truck1.cargo:
        truck1.cargo_addresses[package] = package.location

    # Creates high_priority list for delayed packages so they will be delivered first. Locations in the high priority
    # list are driven to manually. After these packages are dropped off, the truck proceeds with normal delivery method.
    # O(N^2)
    high_priority = []
    while truck1.cargo_count != 0:
        if truck1.time_up:
            break;
        else:
            for i in truck1.cargo:
                if "Delayed" in i.notes and i.deadline != 'EOD':
                    high_priority.append(i)
            while high_priority.__len__() != 0:
                for i in high_priority:
                    truck1.drive_to(i.location, time)
                    truck1.remove_package(i)
                    high_priority.remove(i)
            if len(high_priority) == 0:
                truck1.next_stop(time)

    # Truck is driven to the hub to pick up the package with the updated address.
    # O(1)
    truck1.drive_to(locations.get('0'), time)

    # Time for the truck is advanced for the address for the package to be updated. The address and locations are
    # updated.
    # O(1)
    truck1.wait_for_address_update()
    packages.lookup_item(int(9)).location = locations.get('19')
    packages.lookup_item(int(9)).address = locations.get('19').address
    packages.lookup_item(int(9)).zip = '84111'

    # Truck 1 begins another round of picking up packages.
    # O(N)
    for i in range(1, 41):
        if "truck 2" not in packages.lookup_item(i).notes:
            if packages.lookup_item(i).status == "HUB":
                truck1.add_package(packages.lookup_item(i))
            elif packages.lookup_item(i).status == "DELAYED" and packages.lookup_item(i).package_id != 25:
                truck1.add_package(packages.lookup_item(i))
            elif packages.lookup_item(i).status == "WRONG ADDRESS LISTED":
                truck1.add_package(packages.lookup_item(i))

    # Once again, a manifest of packages and addresses is created specifically for this truck.
    # O(N)
    for package in truck1.cargo:
        truck1.cargo_addresses[package] = package.location

    # Truck begins delivery route again.
    # O(N^2)
    while truck1.cargo_count != 0:
        if truck1.time_up:
            break;
        else:
            truck1.next_stop(time)

    # Truck 2 gets packages and locations associated in its own manifest,
    # O(N)
    for package in truck2.cargo:
        truck2.cargo_addresses[package] = package.location

    # Truck begins its normal delivery route.
    # O(N^2)
    while truck2.cargo_count != 0:
        if truck2.time_up:
            break;
        else:
            truck2.next_stop(time)

    # Truck 2 drives back to the hub for another round of pickups.
    # O(1)
    truck2.drive_to(locations.get('0'), time)

    # Truck 2 begins loading of packages.
    # O(N)
    for i in range(1, 41):
        if packages.lookup_item(i).status == "HUB":
            truck2.add_package(packages.lookup_item(i))
        elif packages.lookup_item(i).status == "DELAYED":
            truck2.add_package(packages.lookup_item(i))
        elif packages.lookup_item(i).status == "WRONG ADDRESS LISTED":
            truck2.add_package(packages.lookup_item(i))

    # Truck 2 creates another manifest of packages and their locations for the new packages.
    # O(N)
    for package in truck2.cargo:
        truck2.cargo_addresses[package] = package.location

    # Truck 2 begins its own version of a high priority delivery route. Once those are delivered, it returns to normal
    # protocol and completes the deliveries.
    # O(N^2)
    while truck2.cargo_count != 0:
        if truck2.time_up:
            break;
        else:
            for i in truck2.cargo:
                if "Delayed" in i.notes and i.deadline != 'EOD':
                    truck2.drive_to(i.location, time)
                    truck2.remove_package(i)
            truck2.next_stop(time)

    # At this point, all packages have been delivered. Depending on the user commands entered, all packages or a
    # specific package is displayed at either the end of the day or at a specific time.
    # O(N) - This is due to the for loops in some of the paths. HOWEVER, it could be O(1) if a specific package is
    # chosen.
    if time == eod_time and package_command == 'all':
        print('End of day status check for all packages:')
        for i in range(1, 41):
            packages.lookup_item(i).print_all(time)
        print('All packages delivered in ', truck1.odometer + truck2.odometer, 'miles.')
    elif time != 'all' and package_command == 'all':
        print('Status check for all packages up to', str(time))
        for i in range(1, 41):
            packages.lookup_item(i).print_all(time)
    elif time == eod_time and package_command != 'all':
        print('End of day status check for package #', packages.lookup_item(int(package_command)).package_id)
        packages.lookup_item(int(package_command)).print_all()
        print('All packages delivered in ', truck1.odometer + truck2.odometer, 'miles.')
    else:
        print('Status check for package #', package_command, 'at', str(time))
        packages.lookup_item(int(package_command)).print_all(time)


# Prints out welcome message.
# O(1)
print("Welcome to the WGUPS Simulation.")
print("Created by Lucas Roberts")
print("")
# Sets end of day time to 11:59 pm.
# O(1)
eod_time = datetime.datetime(2020, 1, 1, 23, 59, 59, 59)
# Takes input from user for which package to query, either all of them or a specific package id.
# O(1)
package_command = input("Which package are you interested in looking up? For all, type 'all' without quotes. Otherwise,"
                        "type a package ID: ")
# Takes input from user for which time they wish to see information on packages. 'all' can be typed to see the package
# info for the end of the day.
# O(1)
time_string = input(
    "What time are you wanting to check the status of the package(s)? type 'all' without quotes or a time in this "
    "format: HH:mm :")
# The time command is formatted for the run_simulation method here.
# O(1)
if time_string == 'all':
    time_command = datetime.datetime(2020, 1, 1, 23, 59, 59, 59)
else:
    time_string = '2020-01-01 ' + time_string + ':00'
    time_command = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")

# Begins running simulation with input parameters given.
run_simulation(time_command, package_command)
