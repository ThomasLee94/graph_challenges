# !python

# essential facts and functionalities of graphs 

from queue import LinkedQueue
from vertex import Vertex

class Graph:
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

        # making vertex_b a neighbour to vertex_a by adding an edge
        vertex_a_obj.add_neighbor(vertex_b_obj, weight)
        # increment edge count
        self.num_edges +=1 
        

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.keys()
    
    def breadth_first_search(self, vertex_key: str)-> object:

        """
            Creates a object with all lengths mapped to vertex_key and returns object
            containing shortest path with verticies.

            Args:
                vertex_key: single str, first iteration of recursive call stack. 
                            Treat as root node, will only be inputted once.
            Returns:

        """

        if n < 1:
            return [vertex_key]

        # check if vertex exists in graph
        if vertex_key not in self.vert_dict:
            raise ValueError("This vertex is not in graph!")

        # Queue to keep track of verticies
        queue = LinkedQueue()
        # keeping track of visits
        visited = set()
        # keeping track of distance between child and parent verticies
        distance = {
            vertex_key: 0
        }
        
        queue.enqueue(vertex_key)
        visited.add(vertex_key)

        while not queue.is_empty():
            # Dequeue front vertex
            vertex = queue.dequeue()

            for neighbour in self.vert_dict[vertex].neighbours:
                if neighbour.id not in visited:
                    # adding str's, not objects
                    queue.enqueue(neighbour.id)
                    visited.add(neighbour.id)
                    # adding distance
                    distance[neighbour.id] = 1 + distance[vertex]
        # returned a filtered list from distance dict of values == n
        func = lambda vertex_key: distance[vertex_key] == n 
        start_list = distance.keys()
        return list(filter(func, start_list))  
    