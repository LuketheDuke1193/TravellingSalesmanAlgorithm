import datetime
class Truck(object):
    def __init__(self, id, location, cargo_count=0, odometer=0):
        self.id = id
        self.cargo_count = cargo_count
        self.location = location
        self.cargo = []
        self.time = datetime.datetime(2020, 1, 1, 8, 00, 00, 00)
        self.odometer = odometer
        self.speed = 18
        self.cargo_addresses = {}

    def add_package(self, package):
        if self.cargo_count >= 16:
            print('Truck ', self.id, ' is full and cannot currently hold anymore packages. (REF Package #', package.package_id)
        else:
            self.cargo.append(package)
            self.cargo_count = self.cargo_count + 1
            package.status_out_for_delivery()
            print('Added package #',package.package_id,' to Truck ',self.id,'- It now has ',self.cargo_count,' packages loaded.')

    def remove_package(self, package):
        if self.cargo_count == 0:
            print('The truck is already empty')
        else:
            package.status_delivered()
            self.cargo.remove(package)
            self.cargo_count = self.cargo_count - 1
            self.cargo_addresses.pop(package)
            print('Truck #', self.id,'just delivered Package #',package.package_id,' to ', self.location.name, 'at ',self.time)

    def add_miles(self, miles):
        self.odometer = self.odometer + miles
        time_advance = miles / ((18 / 60) / 60)
        self.time = self.time + datetime.timedelta(seconds=time_advance)

    def next_stop(self):
        next_location = self.location.closest_neighbor(self.cargo_addresses)
        self.location = next_location[0]
        self.add_miles(float(next_location[1]))

        for Package, Location in self.cargo_addresses.items():
            if Location == self.location:
                package_to_deliver = Package
                break;

        self.remove_package(package_to_deliver)

    def drive_to(self, location):
        distance_to_location = self.location.neighbors[location]
        self.location = location
        self.add_miles(float(distance_to_location))
