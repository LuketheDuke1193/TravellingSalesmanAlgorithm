class Location:
    def __init__(self, id, name, address, distance=0):
        self.id = id
        self.name = name
        self.address = address
        self.distance = distance
        self.neighbors = {}

    # Adds neighbor to neighbors dict with distance as value and location as key
    # O(1)
    def add_neighbor(self, location, distance):
        self.neighbors[location] = distance

    # Finds specified location's closest neighbor that has a package needing delivered.
    # O(N^2)
    def closest_neighbor(self, cargo_list):
        tempList = []
        for Package, Location in cargo_list.items():
            for k in self.neighbors.items():
                if k[0].name == Location.name:
                    tempList.append(k)

        tempList.sort(key=lambda loc: float(loc[1]))
        return tempList[0]

