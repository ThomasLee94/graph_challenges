
# !python

from classes.vertex import Vertex
from classes.stack import LinkedStack
from classes.queue import LinkedQueue

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

    def get_vertex(self, key: str)->object:
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

        # Queue to keep track of verticies, enqueue vertex_a
        queue = LinkedQueue(vertex_a)

        # Keeping track of visits
        visited = set()
        # add vertex_a to set
        visited.add(vertex_a)

        # create dict to store parent and children verticies
        # parent = {
        #   child_vertex: parent_vertex
        # }
        child_parent_path = dict()
        
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
                    child_parent_path[neighbour.id] = vertex
                    
        return child_parent_path
    
    def dfs_recursive(self, vertex_a: str, visit):
            """
                Executes a pre-order depth first search on the given graph.

                Args
                    vertex_a: start vertex
                    visit: given function

                Returns

            """

            while vertex_a is not None:
                visit(vertex_a)
                for neighbour in self.vert_dict[vertex_a].adj_dict_neighbours:
                    self.dfs_recursive(neighbour.id, visit)

            # # check to see if starting node contains data
            # if node is not None:
            #     # Visit this node's data with given function
            #     visit(node.data)
            #     # Traverse left subtree, if it exists
            #     self._traverse_pre_order_recursive(node.left, visit)
            #     # Traverse right subtree, if it exists
            #     self._traverse_pre_order_recursive(node.right, visit)
    
    def _pre_order_dfs_iterative(self, vertex_a: str, vertex_b: str):
            """
                Executes a pre-order depth first search on the given graph.

                Args
                    vertex_a: start vertex
                    vertex_b: to vertex

                Returns

            """

            # Stack to keep track of verticies
            stack = LinkedStack(vertex_a)

            # Keeping track of visits
            visited = set()
            # add vertex_a to set
            visited.add(vertex_a)

            while not stack.is_empty():
                vertex = stack.pop()
                print(vertex)

            # check to see if starting node contains data
            if node is not None:
                # Visit this node's data with given function
                visit(node.data)
                # Traverse left subtree, if it exists
                self._traverse_pre_order_recursive(node.left, visit)
                # Traverse right subtree, if it exists
                self._traverse_pre_order_recursive(node.right, visit)