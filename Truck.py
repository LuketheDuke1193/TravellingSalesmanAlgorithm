# Lucas Roberts #001085316
# C950 WGUPS Project
import datetime


class Truck(object):
    # Creates a truck object with an id, start location, time input from the user, package_id, cargo_count, and odometer
    # O(1)
    def __init__(self, truck_id, location, time_input='all', package_id='all', cargo_count=0, odometer=0):
        self.id = truck_id
        self.cargo_count = cargo_count
        self.location = location
        self.cargo = []
        self.time = datetime.datetime(2020, 1, 1, 8, 00, 00, 00)
        self.odometer = odometer
        self.speed = 18
        self.cargo_addresses = {}
        self.time_input = time_input
        self.package_id = package_id
        self.time_up = False

    # Adds package to a truck object. Checks to make sure the truck isn't full first.
    # O(1)
    def add_package(self, package):
        if self.cargo_count >= 16:
            '''print('Truck ', self.id, ' is full and cannot currently hold anymore packages. (REF Package #', package.package_id)'''
        else:
            self.cargo.append(package)
            package.truck_id = self.id
            self.cargo_count = self.cargo_count + 1
            package.status_out_for_delivery()

    # Removes package from the truck cargo and cargo address list. Also marks time delivered for the package.
    # O(N) due to the .remove() function.
    def remove_package(self, package):
        package.status_delivered()
        self.cargo.remove(package)
        self.cargo_count = self.cargo_count - 1
        self.cargo_addresses.pop(package)
        package.delivered_at_time = self.time

    # Adds miles to the truck object odometer. Also ticks the truck time mechanism along. If the time to stop (issued
    # by the user) is close, the odometer is iterated by 10 second intervals until the time to stop is reached.
    # O(N)
    def add_miles(self, miles, time_to_stop):
        self.odometer = self.odometer + miles
        time_advance = miles / ((18 / 60) / 60)
        if time_to_stop > self.time + datetime.timedelta(seconds=time_advance):
            self.time = self.time + datetime.timedelta(seconds=time_advance)
        else:
            while time_to_stop > self.time:
                self.time = self.time + datetime.timedelta(seconds=10)
            self.time_up = True

    # Finds and goes to next stop for the truck to go to based on the closest neighbor to its current location with a
    # package that needs to be delivered. Delivery time is updated here for a package at the time of removal.
    # O(N^2) due to the closest neighbor function.
    def next_stop(self, time_to_stop):
        while not self.time_up:
            next_location = self.location.closest_neighbor(self.cargo_addresses)
            miles = float(next_location[1])
            self.add_miles(miles, time_to_stop)
            self.location = next_location[0]

            for Package, Location in self.cargo_addresses.items():
                if Location == self.location:
                    package_to_deliver = Package
                    break;
            if self.time_up == False:
                self.remove_package(package_to_deliver)
                package_to_deliver.delivered_at_time = self.time
                break;

    # Drives truck to a specified location, i.e the hub.
    # O(1)
    def drive_to(self, location, time):
        distance_to_location = self.location.neighbors[location]
        self.location = location
        self.add_miles(float(distance_to_location), time)

    # This function serves as a way for a truck object to wait until the specific address update time listed in the
    # project manifest.
    # O(1)
    def wait_for_address_update(self):
        self.time = datetime.datetime(2020, 1, 1, 10, 20, 00, 00)
