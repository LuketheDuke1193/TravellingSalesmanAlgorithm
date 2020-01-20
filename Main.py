#Lucas Roberts #001085316
#C950 WGUPS Project

from HashTable import HashTable
import csv
from Package import Package

packages = HashTable()

#import CSV data for packages
with open('WGUPS Package File.csv') as csvfile:
    readPackageCSV = csv.reader(csvfile, delimiter=',')
    for row in readPackageCSV:
        if len(row) == 6:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.insert(row[0], package)
        else:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            packages.insert(row[0], package)

for i in packages:
    print(i)

#create hash table for package data

#create graph for location data

#load trucks with packages

#create algorithm for delivery of packages