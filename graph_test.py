#!python

from graph import Graph
from vertex import Vertex
import unittest

class GraphTest(unittest.TestCase):

    def test_init(self):
        graph = Graph()
        self.assertEqual(len(graph.vert_dict), 0) 
        self.assertEqual(graph.num_vertices, 0) 
        self.assertEqual(graph.num_edges, 0) 

    def test_add_vertex(self):
        vertex_a = "A"
        graph = Graph()
        graph.add_vertex(vertex_a)
        self.assertEqual(len(graph.vert_dict), 1) 
        vertex_b = "B"
        graph.add_vertex(vertex_b)
        self.assertEqual(len(graph.vert_dict), 2)
    
    def test_get_vertex(self):
        vertex_a = "A"
        graph = Graph()
        graph.add_vertex(vertex_a)
        output_obj = graph.get_vertex(vertex_a)
        self.assertIsInstance(output_obj, Vertex)
    
    def test_add_edge(self):
        pass
    
    def get_vertices(self):
        pass

if __name__ == '__main__':
    unittest.main()
