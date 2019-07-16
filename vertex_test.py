#!python

from graph import Graph
from vertex import Vertex
import unittest

class VertexTest(unittest.TestCase):

    def test_init(self):
        vertex_a = "A"
        vertex_obj = Vertex(vertex_a)
        assert vertex_obj.id is object
        assert len(vertex_obj.adj_dict_neighbours) == 0

    def test_add_neighbour(self):
        # vertex_a is pointing to vertex_b with a weight of 3, "A" -> "B"
        vertex_a = "A"
        vertex_b = "B"
        weight = 3
        vertex_a_obj = Vertex(vertex_a)
        vertex_b_obj = Vertex(vertex_b)
        vertex_a_obj.add_neighbor(vertex_b_obj, weight)
        
        
if __name__ == '__main__':
    unittest.main()
