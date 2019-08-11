#!python


class Vertex(object):
    def __init__(self, vertex: str):
        """
        initialise a vertex and its neighbours.
        """
        # neighbours = {
        #   vertex_obj: weight
        # }

        self.id = vertex
        self.neighbours = {}

    def add_neighbour(self, vertex: object, weight=0):
        """
        add a neighbour along a weighted edge
        """

        if vertex not in self.neighbours.keys():
            # if vertex does not exist, append tuple
            self.neighbours[vertex] = int(weight)

    def get_neighbours(self) -> dict:
        """returns all vertices (nodes) connected to this vertex (node)"""

        return self.neighbours
