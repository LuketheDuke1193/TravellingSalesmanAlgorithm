
class Vertex(object):
    def __init__(self, location):
        self.location = location
        self.distance = 0


class Graph(object):
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = [new_vertex]

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def map_edges_to_vertices(self, origin):
        for vertex in self.adjacency_list.get(origin):
            weight = self.edge_weights.get(origin, vertex).distance
            vertex.distance = weight #FIXME method returns Vertex object instead of float weight.







