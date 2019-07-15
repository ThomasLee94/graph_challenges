#!python
 
class Vertex(object):

    def __init__(self, vertex: str):
        """
        initialize a vertex and its neighbors.
        """

        self.adj_list_neighbours = list()

    def add_neighbor(self, vertex: str, weight=0):
        """
        add a neighbor along a weighted edge
        """

        if vertex not in self.adj_list_neighbours:
            # if vertex does not exist, append tuple
            self.adj_list_neighbours.append((vertex, weight))

    def get_neighbors(self) -> [tuple]:
        """returns all vertices (nodes) connected to this vertex (node)"""

        return self.adj_list_neighbours

    def get_edge_weight(self, vertex: str) -> int:
        """return the weight of this edge"""
        
        for tuple_ in self.adj_list_neighbours:
            if tuple_[0] == vertex:
                return tuple_[1] 