class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, kilo, notes="none", location=None):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.kilo = kilo
        self.notes = notes
        self.status = "HUB"
        self.location = location

    def get_id(self):
        return self.package_id

    def status_out_for_delivery(self):
        self.status = "OUT FOR DELIVERY"

    def status_delivered(self):
        self.status = "DELIVERED"

    def status_delayed(self):
        self.status = "DELAYED"

    def status_wrong_address(self):
        self.status = "WRONG ADDRESS LISTED"
