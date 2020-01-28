import datetime
class Truck(object):
    def __init__(self, id, location, time_input = 'all', package_id = 'all', cargo_count=0, odometer=0):
        self.id = id
        self.cargo_count = cargo_count
        self.location = location
        self.cargo = []
        self.time = datetime.datetime(2020, 1, 1, 8, 00, 00, 00)
        self.odometer = odometer
        self.speed = 18
        self.cargo_addresses = {}
        self.time_input = time_input
        self.package_id = package_id
        self.cargo_history = self.cargo

# Adds package to a truck object. Checks to make sure the truck isn't full first.
# O(1)
    def add_package(self, package):
        if self.cargo_count >= 16:
            '''print('Truck ', self.id, ' is full and cannot currently hold anymore packages. (REF Package #', package.package_id)'''
        else:
            self.cargo.append(package)
            self.cargo_history.append(package)
            self.cargo_count = self.cargo_count + 1
            package.status_out_for_delivery()
            '''print('Added package #',package.package_id,' to Truck ',self.id,'- It now has ',self.cargo_count,' packages loaded.')'''

# Removes package from the truck cargo and cargo address list.
# O(N) due to the .remove() function.
    def remove_package(self, package):
        if self.cargo_count == 0:
            '''print('The truck is already empty')'''
        else:
            package.status_delivered()
            self.cargo.remove(package)
            self.cargo_count = self.cargo_count - 1
            self.cargo_addresses.pop(package)
            '''print('Truck #', self.id,'just delivered Package #',package.package_id,' to ', self.location.name, 'at ',self.time)'''

# Adds miles to the truck object odometer
# O(N)
    def add_miles(self, miles):
        self.odometer = self.odometer + miles
        time_advance = miles / ((18 / 60) / 60)
        self.time = self.time + datetime.timedelta(seconds=time_advance)

# Finds and goes to next stop for the truck to go to based on the closest neighbor to its current location with a package that needs
# to be delivered. O(N^2) due to the closest neighbor function.
    def next_stop(self, list):
        next_location = self.location.closest_neighbor(self.cargo_addresses)
        miles = float(next_location[1])
        if self.time_input == 'all':
            self.location = next_location[0]
            self.add_miles(miles)

            for Package, Location in self.cargo_addresses.items():
                if Location == self.location:
                    package_to_deliver = Package
                    break;

            self.remove_package(package_to_deliver)
        else:
            while self.time < self.time_input:
                self.location = next_location[0]
                self.add_miles(miles)

                for Package, Location in self.cargo_addresses.items():
                    if Location == self.location:
                        package_to_deliver = Package
                        break;

                self.remove_package(package_to_deliver)
            if self.package_id == 'all':
                for package in self.cargo_history:
                    list.append(package)
            else:
                for i in self.cargo_history:
                    if i.package_id == self.package_id:
                        i.print_all()

# Drives truck to a specified location, i.e the hub.
# O(1)
    def drive_to(self, location):
        distance_to_location = self.location.neighbors[location]
        self.location = location
        self.add_miles(float(distance_to_location))
