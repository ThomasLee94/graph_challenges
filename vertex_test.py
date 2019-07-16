#!python

from vertex import Vertex
import unittest

class VertexTest(unittest.TestCase):

    def test_init(self):
        vertex_a = "A"
        vertex_obj = Vertex(vertex_a)
        # checking if vertex_obj is saved properly
        assert isinstance(vertex_obj.id, str)
        assert len(vertex_obj.adj_dict_neighbours) == 0

    def test_add_neighbour(self):
        # vertex_a is pointing to vertex_b with a weight of 3, "A" -> "B"
        vertex_a = "A"
        vertex_b = "B"
        weight = 3
        vertex_a_obj = Vertex(vertex_a)
        vertex_b_obj = Vertex(vertex_b)
        vertex_a_obj.add_neighbor(vertex_b_obj, weight)
        assert len(vertex_a_obj.adj_dict_neighbours) == 1
        assert vertex_a_obj.adj_dict_neighbours[vertex_b_obj] == weight

    def test_get_neighbours(self):
        vertex_a = "A"
        vertex_b = "B"
        weight = 3
        vertex_a_obj = Vertex(vertex_a)
        vertex_b_obj = Vertex(vertex_b)
        vertex_a_obj.add_neighbor(vertex_b_obj, weight)
        dict_output = vertex_a_obj.get_neighbors()
        assert isinstance(dict_output, dict)
        assert len(dict_output) == 1
        assert dict_output[vertex_b_obj] == 3

if __name__ == '__main__':
    unittest.main()
