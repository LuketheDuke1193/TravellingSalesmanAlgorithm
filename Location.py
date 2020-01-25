class Location:
    def __init__(self, id, name, address, distance=0):
        self.id = id
        self.name = name
        self.address = address
        self.distance = distance
        self.neighbors = {}

    def add_neighbor(self, location, distance):
        self.neighbors[location] = distance

    def closest_neighbor(self, cargo_list):
        tempList = []
        for Package, Location in cargo_list.items():
            for k in self.neighbors.items():
                if k[0].name == Location.name:
                    tempList.append(k)

        sorted(tempList, key=lambda loc: loc[0].distance)
        return tempList[0]

