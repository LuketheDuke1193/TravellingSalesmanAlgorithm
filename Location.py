# Lucas Roberts #001085316
# C950 WGUPS Project

class Location:
    # Creates location with id, name, address, and a default distance of 0. This number will change for locations inside
    # the neighbors dictionary. The neighbors dictionary includes a location's specific neighbors and their distances
    # from the location.
    # O(1)
    def __init__(self, location_id, name, address, distance=0):
        self.id = location_id
        self.name = name
        self.address = address
        self.distance = distance
        self.neighbors = {}

    # Adds neighbor to neighbors dict with distance as value and location as key.
    # O(1)
    def add_neighbor(self, location, distance):
        self.neighbors[location] = distance

    # Finds specified location's closest neighbor that has a package needing delivered. Returns a list of all of the
    # neighbors that have packages needing delivered and sorts them by distance. Returns the shortest distance neighbor.
    # O(N^2) - the sort is O(n log n) but since O(N^2) is larger, we use it.
    def closest_neighbor(self, cargo_list):
        temp_list = []
        for Package, Location in cargo_list.items():
            for k in self.neighbors.items():
                if k[0].name == Location.name:
                    temp_list.append(k)

        temp_list.sort(key=lambda loc: float(loc[1]))
        return temp_list[0]

