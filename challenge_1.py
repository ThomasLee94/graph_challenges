from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse

def challenge_1(file: str) -> Graph:
    graph_type, verticies, edges_str = graph_from_file(file)

    # Create graph depending on type
    if graph_type == "G":
        graph = Graph()
    elif graph_type == "D":
        graph = Digraph()
    else:
        raise ValueError("Graph type is not specified!")
    
    # fill graph instance with edges and verticies
    fill(graph, verticies, edges_str)
    
    # print vertices
    print(f"Verticies: {len(graph.get_vertices())}")
    
    # print edges
    print(f"Edges: {graph.num_edges}")
   
    # print edge list
    for vertex in graph.vert_dict:
        vert = graph.get_vertex(vertex) 
        for neighbour, weight in vert.adj_dict_neighbours.items():
            print(f"({vert.id}, {neighbour.id}, {weight})")

challenge_1("graph_data_1.txt")