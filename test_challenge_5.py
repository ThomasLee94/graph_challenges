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

        graph = Graph()
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_edge(vertex_a, vertex_b)
        self.assertEqual(graph.num_edges, 1)

        vertex_a_obj = graph.vert_dict[vertex_a]
        vertex_b_obj = graph.vert_dict[vertex_b]

        # check if vertex_a & vertex_b are neighbours of each other.
        self.assertIn(vertex_a_obj, vertex_b_obj.neighbours)
        self.assertIn(vertex_b_obj, vertex_a_obj.neighbours)

    def test_shortest_path(self):
        graph = Graph()
        verticies = ["1", "2", "3", "4", "5"]
        edges = [
            ("1", "2"),
            ("1", "4"),
            ("2", "3"),
            ("2", "4"),
            ("2", "5"),
            ("3", "5"),
        ]

        # add verticies to path
        for vertex in verticies:
            graph.add_vertex(vertex)

        # add edges to graph
        for tuple_edge in edges:
            graph.add_edge(tuple_edge[0], tuple_edge[1])

        from_vertex = "1"
        to_vertex = "5"

        output = graph.breadth_first_search(from_vertex, to_vertex)
        expected_output = {'2': '1', '4': '1', '3': '2', '5': '2'}

        # output is used to calculate the shortest path
        self.assertEqual(output, expected_output)

    def test_non_eulerian(self):
        """
            Creates an undirected graph that does not contain a Eulerian 
            cycle. 
        """
        vertex_a = "A"
        vertex_b = "B"
        vertex_c = "C"
        vertex_d = "D"
        vertex_e = "E"

        graph = Graph()
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_vertex(vertex_c)
        graph.add_vertex(vertex_d)
        graph.add_vertex(vertex_e)
        graph.add_edge(vertex_a, vertex_b)
        graph.add_edge(vertex_a, vertex_e)
        graph.add_edge(vertex_b, vertex_c)
        graph.add_edge(vertex_c, vertex_d)

        self.assertEqual(graph.is_eulerian(), False)

    def test_eulerian(self):
        """
            Creates an undirected graph thatdoes contain a Eulerian
            cycle.  
        """

        vertex_a = "A"
        vertex_b = "B"
        vertex_c = "C"
        vertex_d = "D"
        vertex_e = "E"

        graph = Graph()
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_vertex(vertex_c)
        graph.add_vertex(vertex_d)
        graph.add_vertex(vertex_e)
        graph.add_edge(vertex_a, vertex_b)
        graph.add_edge(vertex_a, vertex_e)
        graph.add_edge(vertex_b, vertex_c)
        graph.add_edge(vertex_c, vertex_d)
        graph.add_edge(vertex_d, vertex_e)

        self.assertEqual(graph.is_eulerian(), True)


if __name__ == '__main__':
    unittest.main()
