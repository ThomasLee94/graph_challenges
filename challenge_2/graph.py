# !python

from queue import LinkedQueue
from vertex import Vertex

class Graph(object):
    """ essential facts and functionalities of an undirected graph"""

    def __init__(self):
        """ 
        initialises a graph object with an empty dict.
        """

        # vert_dict:
        # {
        #   "key": vertex_obj
        # }

        self.vert_dict = {}
        self.num_vertices = 0
        self.num_edges = 0

    def add_vertex(self, key: str) -> object:
        """
        add a new vertex object to the graph with
        the given key and return the vertex
        """

        if key not in self.vert_dict.keys():
            # create new vertex and add to vertex dict
            self.vert_dict[key] = Vertex(key)
            # increment number of verticles
            self.num_vertices += 1
        return self.vert_dict[key]

    def get_vertex(self, key: str):
        """return the vertex if it exists"""

        return self.vert_dict[key]

    def add_edge(self, vertex_a: str, vertex_b: str, weight=0):
        """
        add an edge from vertex a to vertex b with a weight
        """
        
        # check if vertices exist in graph
        if vertex_a not in self.vert_dict.keys():
            # raise error if vertex_a does not exist
            raise ValueError("This vertex does not exist in graph!")

        if vertex_b not in self.vert_dict.keys():
            # raise error if vertex_b does not exist
            raise ValueError("This vertex does not exist in graph!")

        vertex_a_obj = self.vert_dict[vertex_a]
        vertex_b_obj = self.vert_dict[vertex_b]

        # adding edges in both ways
        vertex_a_obj.add_neighbour(vertex_b_obj, weight)
        vertex_b_obj.add_neighbour(vertex_a_obj, weight)

        # increment edge count
        self.num_edges +=1 
        

    def get_vertices(self):
        """return all the vertices in the graph"""

        return self.vert_dict.keys()
    
    def get_edges(self, vertex: str) -> [str]:
        """ Returns all of the edges of given vertex """
        
        return self.vert_dict[vertex].adj_dict_neighbours
            
    
    def breadth_first_search(self, vertex_a: str, vertex_b: str)-> object:

        """
            Executes a breadth for search on the given graph. 

            Args:
                vertex_a: from vertex.
                vertex_b: to vertex.
            Returns:
                a dict of containing parent and child verticies.
        """

        # Check if verticies exists in graph
        if vertex_a not in self.vert_dict:
            if vertex_b not in self.vert_dict:
                raise ValueError("This vertex is not in graph!")

        # Queue to keep track of verticies
        # tail is front of queue
        queue = LinkedQueue()

        # Keeping track of visits
        visited = set()

        # create dict to store parent and children verticies
        parent = dict()
        
        queue.enqueue(vertex_a)
        visited.add(vertex_a)

        # Iterating through queue
        while not queue.is_empty():
            # Dequeue front vertex
            vertex = queue.dequeue()

            for neighbour in self.vert_dict[vertex].adj_dict_neighbours:
                if neighbour.id not in visited:
                    # adding str's, not objects
                    queue.enqueue(neighbour.id)
                    visited.add(neighbour.id)
                    # creating key-value pair in parent dict
                    parent[neighbour.id] = vertex
                    
        return parent
    