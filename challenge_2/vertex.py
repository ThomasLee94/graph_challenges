#!python
 
class Vertex(object):

    def __init__(self, vertex: str):
        """
        initialise a vertex and its neighbours.
        """
        # adj_dict_neighbours = {
        #   vertex_obj: weight
        # }

        self.id = vertex
        self.adj_dict_neighbours = {}

    def add_neighbour(self, vertex: Vertex, weight=0):
        """
        add a neighbour along a weighted edge
        """

        if vertex not in self.adj_dict_neighbours.keys():
            # if vertex does not exist, append tuple
            self.adj_dict_neighbours[vertex] = weight

    def get_neighbours(self) -> dict:
        """returns all vertices (nodes) connected to this vertex (node)"""

        return self.adj_dict_neighbours
