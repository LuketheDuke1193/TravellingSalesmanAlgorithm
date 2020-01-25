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

for k,v in locations.items():
    for i in range(0, 26):
        v.add_neighbor(locations.get(str(i)), rows[i][int(v.id)+3])

# Associates location to each package.
# O(N^2)
for i in range(1,40):
    package_to_mark = packages.lookup_item(i)
    for k,v in locations.items():
        if package_to_mark.address in v.address:
            package_to_mark.location = v


truck1 = Truck(1, locations.get(str(0)))
truck2 = Truck(2, locations.get(str(0)))

# First round of adding packages
# O(N)
for i in range(1, 40):
    package_being_loaded = packages.lookup_item(i)
    if "truck 2" in packages.lookup_item(i).notes:
        truck2.add_package(packages.lookup_item(i))
        '''print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',packages.lookup_item(i).address, 'onto truck 2')'''
    elif "Delayed" in packages.lookup_item(i).notes:
        packages.lookup_item(i).status_delayed()
    elif "Must be" in packages.lookup_item(i).notes or packages.lookup_item(i).package_id in (13, 15, 19):
        truck1.add_package(packages.lookup_item(i))
        '''print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',packages.lookup_item(i).address, 'onto truck 1')'''
    elif packages.lookup_item(i).deadline != "EOD":
        truck1.add_package(packages.lookup_item(i))
        '''print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',packages.lookup_item(i).address, 'onto truck 1')'''
    elif packages.lookup_item(i).deadline == "EOD":
        truck2.add_package(packages.lookup_item(i))
        '''print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',packages.lookup_item(i).address, 'onto truck 2')'''

print(truck1.cargo_count)
print(truck2.cargo_count)

while truck1.cargo_count != 16: #FIXME add in constraints from previous round of package loading so that items that can only be on truck2 don't get added to truck 1.
    for i in range(1, 40):
        if packages.lookup_item(i).status == "HUB":
            truck1.add_package(packages.lookup_item(i))
            packages.lookup_item(i).status_out_for_delivery()
            '''print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',packages.lookup_item(i).address, 'onto truck 1')'''

while truck2.cargo_count != 16:
    for i in range(1, 40):
        if packages.lookup_item(i).status == "HUB":
            truck2.add_package(packages.lookup_item(i))
            packages.lookup_item(i).status_out_for_delivery()
            '''print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',packages.lookup_item(i).address, 'onto truck 1')'''

print(truck1.cargo_count)
print(truck2.cargo_count)


for package in truck1.cargo:
    truck1.cargo_addresses[package] = package.location

print(truck1.location.closest_neighbor(truck1.cargo_addresses))





















