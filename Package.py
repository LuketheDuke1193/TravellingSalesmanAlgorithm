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

    #Returns package_id
    # O(1)
    def get_id(self):
        return self.package_id

    # Changes status for specified package
    # O(1)
    def status_out_for_delivery(self):
        self.status = "OUT FOR DELIVERY"

    # Changes status for specified package
    # O(1)
    def status_delivered(self):
        self.status = "DELIVERED"

    # Changes status for specified package
    # O(1)
    def status_delayed(self):
        self.status = "DELAYED"

    # Changes status for specified package
    # O(1)
    def status_wrong_address(self):
        self.status = "WRONG ADDRESS LISTED"

    def print_all(self):
        print('Package #',self.package_id, '-',self.address, self.deadline, self.city, self.zip, self.kilo, self.status)