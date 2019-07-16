#!python

from graph import Graph
from vertex import Vertex
import unittest

class GraphTest(unittest.TestCase):

    def test_init(self):
        graph = Graph()
        assert len(graph.vert_dict) == 0 
        assert graph.num_vertices == 0
        assert graph.num_edges == 0

    def test_add_vertex(self):
        vertex_a = "A"
        graph = Graph()
        graph.add_vertex(vertex_a)
        assert len(graph.vert_dict) == 1
        vertex_b = "B"
        graph.add_vertex(vertex_b)
        assert len(graph.add_vertex) == 2

if __name__ == '__main__':
    unittest.main()
