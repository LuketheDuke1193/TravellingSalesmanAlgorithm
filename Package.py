class Package(object):
    def __init__(self, package_id, address, city, state, zip, deadline, kilo, notes = "none"):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.kilo = kilo
        self.notes = notes

    def get_id(self):
        return self.package_id