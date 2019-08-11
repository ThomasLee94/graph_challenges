from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
from classes.vertex import Vertex
import unittest


class VertexTest(unittest.TestCase):
    def test_init(self):
        vertex_a = "A"
        vertex_obj = Vertex(vertex_a)
        # checking if vertex_obj is saved properly
        self.assertIsInstance(vertex_obj.id, str)
        self.assertEqual(len(vertex_obj.neighbours), 0)

    def test_add_neighbour(self):
        # vertex_a is pointing to vertex_b with a weight of 3, "A" -> "B"
        vertex_a = "A"
        vertex_b = "B"
        weight = 3
        vertex_a_obj = Vertex(vertex_a)
        vertex_b_obj = Vertex(vertex_b)
        vertex_a_obj.add_neighbour(vertex_b_obj, weight)
        self.assertEqual(len(vertex_a_obj.neighbours), 1)
        self.assertEqual(vertex_a_obj.neighbours[vertex_b_obj], weight)

    def test_get_neighbours(self):
        vertex_a = "A"
        vertex_b = "B"
        weight = 3
        vertex_a_obj = Vertex(vertex_a)
        vertex_b_obj = Vertex(vertex_b)
        vertex_a_obj.add_neighbour(vertex_b_obj, weight)
        dict_output = vertex_a_obj.get_neighbours()
        self.assertIsInstance(dict_output, dict)
        self.assertEqual(len(dict_output), 1)
        self.assertEqual(dict_output[vertex_b_obj], 3)


class DigraphTest(unittest.TestCase):
    def test_init(self):
        graph = Digraph()
        self.assertEqual(len(graph.vert_dict), 0)
        self.assertEqual(graph.num_vertices, 0)
        self.assertEqual(graph.num_edges, 0)

    def test_add_vertex(self):
        vertex_a = "A"
        graph = Digraph()
        graph.add_vertex(vertex_a)
        self.assertEqual(len(graph.vert_dict), 1)
        self.assertEqual(graph.num_vertices, 1)
        vertex_b = "B"
        graph.add_vertex(vertex_b)
        self.assertEqual(len(graph.vert_dict), 2)
        self.assertEqual(graph.num_vertices, 2)

    def test_get_vertex(self):
        vertex_a = "A"
        graph = Digraph()
        graph.add_vertex(vertex_a)
        output_obj = graph.get_vertex(vertex_a)
        self.assertIsInstance(output_obj, Vertex)

    def test_add_edge(self):
        vertex_a = "A"
        vertex_b = "B"
        weight = 3
        graph = Digraph()
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_edge(vertex_a, vertex_b, weight)
        self.assertEqual(graph.num_edges, 1)

        # test for correct adjacency list (neighbours)
        for vertex in graph.vert_dict:
            vert = graph.get_vertex(vertex)
            for neighbour, weight_ in vert.neighbours.items():
                self.assertEqual(vertex_b, neighbour.id)
                self.assertEqual(weight, weight_)


if __name__ == '__main__':
    unittest.main()
