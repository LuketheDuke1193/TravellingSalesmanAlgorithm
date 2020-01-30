# Lucas Roberts #001085316
# C950 WGUPS Project

class Package:
    # Creates a package object with an id, address, location, deadline, kilo, special notes, status, truck id, and
    # delivered at time that is updated upon delivery.
    # O(1)
    def __init__(self, package_id, address, city, state, zip_code, deadline, kilo, notes="none", location=None):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.deadline = deadline
        self.kilo = kilo
        self.notes = notes
        self.status = "HUB"
        self.location = location
        self.truck_id = None
        self.delivered_at_time = None

    # Returns package_id
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

    # Prints information for the package. If the time input is the default (None), the info is printed in an 'as of X'
    # format. Otherwise, the info is printed with a delivery time. All times are printed in HH:MM format with am or pm.
    # O(1)
    def print_all(self, time=None):
        if time is not None:
            time_string = time.strftime("%H:%M %p")
        if self.status == "DELIVERED":
            time_string = self.delivered_at_time.strftime("%H:%M %p")
            print('Package #', self.package_id, '-', self.address, self.city, self.zip, 'Deadline:', self.deadline,
                  'Weight:', self.kilo, 'Status:', self.status, 'at', time_string, 'by Truck', self.truck_id)
        else:
            print('Package #', self.package_id, '-', self.address, self.city, self.zip, 'Deadline:', self.deadline,
                  'Weight:', self.kilo, 'Status:', self.status, 'as of', time_string)
