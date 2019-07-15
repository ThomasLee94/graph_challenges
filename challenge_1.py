from read_data import read_file
from vertex import Vertex
from graph import Graph

def challenge_1():
     # Challenge 1: Create the graph

     vertex = list()
     weight = list()

    graph = Graph()

    # Add your friends
    graph.add_vertex("Friend 1")
    graph.add_vertex("Friend 2")
    graph.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))