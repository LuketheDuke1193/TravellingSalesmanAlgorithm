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

    def add_package(self, package):
        if self.cargo_count >= 16:
            print('The truck is full and cannot currently hold anymore packages.')
        else:
            self.cargo.append(package)
            self.cargo_count = self.cargo_count + 1

    def remove_package(self, package):
        if self.cargoCount == 0:
            print('The truck is already empty')
        else:
            self.cargo.remove(package)
            self.cargo_count = self.cargo_count - 1

    def add_miles(self, miles):
        self.odometer = self.odometer + miles
        time_advance = (miles / 60) / 60
        self.time = self.time + datetime.timedelta(0, time_advance)
