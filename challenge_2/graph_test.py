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
        self.assertEqual(graph.num_vertices, 1)
        vertex_b = "B"
        graph.add_vertex(vertex_b)
        self.assertEqual(len(graph.vert_dict), 2)
        self.assertEqual(graph.num_vertices, 2)
    
    def test_get_vertex(self):
        vertex_a = "A"
        graph = Graph()
        graph.add_vertex(vertex_a)
        output_obj = graph.get_vertex(vertex_a)
        self.assertIsInstance(output_obj, Vertex)
    
    def test_add_edge(self):
        vertex_a = "A"
        vertex_b = "B"
        weight = 3
        graph = Graph()
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_edge(vertex_a, vertex_b, weight)
        self.assertEqual(graph.num_edges, 1)
        
        # test for correct adjacency list (neighbours)
        for vertex in graph.vert_dict:
            vert = graph.get_vertex(vertex)
            for neighbour, weight_ in vert.adj_dict_neighbours.items():
                self.assertEqual(vertex_b, neighbour.id)
                self.assertEqual(weight, weight_)
    
    def test_shortest_path(self):
        graph = Graph()
        verticies = ["1","2","3","4","5"]
        edges = [("1","2"),("1","4"),("2","3"),("2","4"),("2","5"),("3","5")]

        # add verticies to path
        for vertex in verticies:
            graph.add_vertex(vertex)
        
        # add edges to graph
        for tuple_edge in edges:
            graph.add_edge(tuple_edge[0], tuple_edge[1])
        
        output = graph.breadth_first_search("1","5")
        expected_output = {'2': '1', '4': '1', '3': '2', '5': '2'}

        self.assertEqual(output, expected_output)
        
        
        
        
if __name__ == '__main__':
    unittest.main()
