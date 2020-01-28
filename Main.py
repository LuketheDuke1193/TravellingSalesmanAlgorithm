# Lucas Roberts #001085316
# C950 WGUPS Project

from HashTable import HashTable
import csv

from Location import Location
from Package import Package

# create hash table for package data
from Truck import Truck

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




def run_simulation(time='all', package='all'):
    truck1 = Truck(1, locations.get(str(0)))
    truck2 = Truck(2, locations.get(str(0)))
    list_to_return = []

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

    print(truck1.cargo_count)
    print(truck2.cargo_count)

    # O(N^2)
    while truck1.cargo_count != 16:
        for i in range(1, 41):
            if "truck 2" not in packages.lookup_item(i).notes:
                if packages.lookup_item(i).status == "HUB":
                    truck1.add_package(packages.lookup_item(i))

    # O(N^2)
    while truck2.cargo_count != 16:
        for i in range(1, 40):
            if packages.lookup_item(i).status == "HUB":
                truck2.add_package(packages.lookup_item(i))

    print(truck1.cargo_count)
    print(truck2.cargo_count)

    # O(N)
    for package in truck1.cargo:
        truck1.cargo_addresses[package] = package.location

    # O(N)
    while truck1.cargo_count != 0:
        truck1.next_stop(list_to_return)

    for i in range(1, 40):
        print('Package #', packages.lookup_item(i).package_id, 'is', packages.lookup_item(i).status)

    truck1.drive_to(locations.get('0'))

    # O(N)
    for i in range(1, 41):
        if "truck 2" not in packages.lookup_item(i).notes:
            if packages.lookup_item(i).status == "HUB":
                truck1.add_package(packages.lookup_item(i))
            elif packages.lookup_item(i).status == "DELAYED":
                truck1.add_package(packages.lookup_item(i))
            elif packages.lookup_item(i).status == "WRONG ADDRESS LISTED":
                truck1.add_package(packages.lookup_item(i))

    print(truck1.cargo_count)

    # O(N)
    for package in truck1.cargo:
        truck1.cargo_addresses[package] = package.location

    # O(N)
    while truck1.cargo_count != 0:
        truck1.next_stop(list_to_return)

    # O(N)
    for package in truck2.cargo:
        truck2.cargo_addresses[package] = package.location

    # O(N)
    while truck2.cargo_count != 0:
        truck2.next_stop(list_to_return)

    truck2.drive_to(locations.get('0'))

    # O(N)
    for i in range(1, 41):
        if packages.lookup_item(i).status == "HUB":
            truck2.add_package(packages.lookup_item(i))
        elif packages.lookup_item(i).status == "DELAYED":
            truck2.add_package(packages.lookup_item(i))
        elif packages.lookup_item(i).status == "WRONG ADDRESS LISTED":
            truck2.add_package(packages.lookup_item(i))

    # O(N)
    for package in truck2.cargo:
        truck2.cargo_addresses[package] = package.location

    # O(N)
    while truck2.cargo_count != 0:
        truck2.next_stop(list_to_return)

    # O(N)
    for i in range(1, 41):
        print(packages.lookup_item(i).status)

    print('All packages delivered on two trucks in a total of', truck1.odometer + truck2.odometer, 'miles!')
    for package in list_to_return:
        package.print_all()


print("Welcome to the WGUPS Simulation.")
print("Created by Lucas Roberts")
print("")
package_command = input("Which package are you interested in looking up? For all, type 'all' without quotes.")
time_command = input("What time are you wanting to check the status of the package(s)?")

run_simulation(time_command, package_command)
