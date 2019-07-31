from classes.vertex import Vertex
from classes.queue import LinkedQueue
import classes.util.read_data as read_data
from classes.priority_queue import PriorityQueue
import math


class Graph(Vertex):
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

    # from classes.util.read_data import string_to_tuple
    def get_vertex(self, key: str) -> object:
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
        self.num_edges += 1

    def get_vertices(self):
        """return all the vertices in the graph"""

        return self.vert_dict.keys()

    def get_edges(self, vertex: str) -> [str]:
        """ Returns all of the edges of given vertex """

        return self.vert_dict[vertex].neighbours

    def breadth_first_search(self, vertex_a: str, vertex_b: str) -> object:

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
            raise ValueError(f"vertex {vertex_a} is not in graph!")
        if vertex_b not in self.vert_dict:
            raise ValueError(f"vertex {vertex_b} is not in graph!")

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

            # sorting keys in adjacency list to evaluate vertex.id
            keys = self.vert_dict[vertex].neighbours.keys()
            sorted_keys = sorted(keys, key=lambda vertex: vertex.id)
            # looping through neighbours
            for neighbour in sorted_keys:
                if neighbour.id not in visited:
                    # adding str's, not objects
                    queue.enqueue(neighbour.id)
                    visited.add(neighbour.id)
                    # creating key-value pair in parent dict
                    child_parent_path[neighbour.id] = vertex

        return child_parent_path

    def dfs_recursive(
        self,
        vertex_a: str,
        vertex_b: str,
        visited_list: [str],
        visited_set,
        custom_func,
    ) -> (bool, [str]):
        """
                Executes a depth first search on the given graph.
                Args
                    vertex_a: start vertex
                    vertex_b: to vertex
                    visited_list: keeps track of visited verticies in order of traversal
                    visited: set method to keep track of visited verticies.
                    custom_func: execute custom function on vertex
                Returns
                    If vertex_b is in any branch from vertex_a: return (True, verticies_list)
                    If vertex_b not in any branch from vertex_a: return (False, verticies_list) 
            """

        # Check if verticies exists in graph
        if vertex_a not in self.vert_dict:
            raise ValueError(f"vertex {vertex_a} is not in graph!")
        if vertex_b not in self.vert_dict:
            raise ValueError(f"vertex {vertex_b} is not in graph!")

        if vertex_a in self.vert_dict and vertex_a not in visited_set:
            # Add vertex_a to set
            visited_set.add(vertex_a)
            # add vertex to visited list in order
            visited_list.append(vertex_a)
            # execute custome_func:
            custom_func(vertex_a)
            # if vertex_b is found
            if vertex_a == vertex_b:
                return (True, visited_list)
            # add neighbours of vertex_a in stack
            for neighbour in self.vert_dict[vertex_a].neighbours:
                # visit neighbours recursively
                return self.dfs_recursive(
                    neighbour.id,
                    vertex_b,
                    visited_list,
                    visited_set,
                    custom_func,
                )

        # Catch all
        return (False, visited_list)

    def prim(self, vertex_a: str, vertex_b: str) -> object:
        """ 
            An implementation of Primms greedy algorithm, it will return the minimum spanning tree
            of a graph. 
            Args
                vertex_a: start vertex
                vertex_b: end vertex
            Returns
        """

        # Check if verticies exists in graph
        if vertex_a not in self.vert_dict:
            raise ValueError(f"vertex {vertex_a} is not in graph!")
        if vertex_b not in self.vert_dict:
            raise ValueError(f"vertex {vertex_b} is not in graph!")

        # keep track of verticies with priority queue
        pqueue = PriorityQueue()
        # infinity
        infinity = math.inf
        # distance dict
        distance = {vertex_a: 0}
        # previous dict
        previous = dict()

        # loop through all verticies in graph
        for vertex in self.vert_dict:
            if vertex != vertex_a:
                # make path for vertex infinity by default
                distance[vertex] = infinity
            vertex_obj = self.vert_dict[vertex]
            # enqueueing vertex with weight
            pqueue.push(vertex, distance[vertex])

        # while queue is not empty
        while pqueue:
            # dequeue smallest distance[vertex]
            vertex = pqueue.pop()
            vertex_obj = self.vert_dict[vertex]
            # looping through neighbours of vertex
            for neighbour in vertex_obj.neighbours:
                # finding alternate distances
                print(distance[vertex])
                print(vertex_obj.neighbours[neighbour])
                print(type(distance[vertex]))
                print(type(vertex_obj.neighbours[neighbour]))
                # Do not care about edge accumilation, do not add edge weight of neighbbour
                alt = distance[vertex]
                if alt < distance[neighbour]:
                    distance[neighbour] = alt
                    previous[neighbour] = vertex

        return distance, previous

    def min_weight_path(self, vertex_a: str, vertex_b: str) -> object:
        """ 
            An implementation of Dijkstra greedy algorithm, it will return the shortest 
            weighted path from vertex_a to vertex_b. 
            Args
                vertex_a: start vertex
                vertex_b: end vertex
            Returns
        """

        # Check if verticies exists in graph
        if vertex_a not in self.vert_dict:
            raise ValueError(f"vertex {vertex_a} is not in graph!")
        if vertex_b not in self.vert_dict:
            raise ValueError(f"vertex {vertex_b} is not in graph!")

        # keep track of verticies with priority queue
        pqueue = PriorityQueue()
        # infinity
        infinity = math.inf
        # distance dict
        distance = {vertex_a: 0}
        # previous dict
        previous = dict()

        # loop through all verticies in graph
        for vertex in self.vert_dict:
            if vertex != vertex_a:
                # make path for vertex infinity by default
                distance[vertex] = infinity
            vertex_obj = self.vert_dict[vertex]
            # enqueueing vertex with weight
            pqueue.push(vertex, distance[vertex])

        # while queue is not empty
        while pqueue:
            # dequeue smallest distance[vertex]
            vertex = pqueue.pop()
            vertex_obj = self.vert_dict[vertex]
            # looping through neighbours of vertex
            for neighbour in vertex_obj.neighbours:
                # finding alternate distances
                print(distance[vertex])
                print(vertex_obj.neighbours[neighbour])
                print(type(distance[vertex]))
                print(type(vertex_obj.neighbours[neighbour]))

                alt = distance[vertex] + vertex_obj.neighbours[neighbour]
                if alt < distance[neighbour]:
                    distance[neighbour] = alt
                    previous[neighbour] = vertex

        return distance, previous


def fill(graph: Graph, verticies: [str], edges_and_weight: [str]) -> Graph:
    """
        Fills graph based on input verticies and edges and optional weights 
    """

    # creating edge_list iterable
    edge_list = list()
    for edge in edges_and_weight:
        edge_list.append(read_data.string_to_tuple(edge))

    # add verticies
    for vertex in verticies:
        graph.add_vertex(vertex)

    # add edges and weights
    for tuple_ in edge_list:
        # if weight was not given, default to 0
        if len(tuple_) == 2:
            graph.add_edge(tuple_[0], tuple_[1], 0)
        else:
            graph.add_edge(tuple_[0], tuple_[1], tuple_[2])

    return graph
