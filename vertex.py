#!python
 
class Vertex(object):

    def __init__(self, vertex: str):
        """
        initialize a vertex and its neighbors.
        """
        # {
        #   "key": weight
        # }

        self.id = vertex
        self.adj_dict_neighbours = {}

    def add_neighbor(self, vertex: object, weight=0):
        """
        add a neighbor along a weighted edge
        """

        if vertex not in self.adj_dict_neighbours.keys():
            # if vertex does not exist, append tuple
            self.adj_dict_neighbours[vertex] = weight

    def get_neighbors(self) -> dict:
        """returns all vertices (nodes) connected to this vertex (node)"""

        return self.adj_dict_neighbours

    def get_edge_weight(self, vertex: str) -> int:
        """return the weight of this edge"""
        
        for tuple_ in self.adj_dict_neighbours:
            if tuple_[0] == vertex:
                return tuple_[1] 