from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse

def challenge_2(file: str, vertex_a: str, vertex_b: str) -> Graph:
    graph_type, verticies, edges_str = graph_from_file(file)

    # Create graph depending on type
    if graph_type == "G":
        graph = Graph()
    if graph_type == "D":
        graph = Digraph()
    
    # fill graph instance with edges and verticies
    fill(graph, verticies, edges_str)
    
    # getting parent dict
    dict_ = graph.breadth_first_search(vertex_a,vertex_b)

    parent = dict_[vertex_b]
    output = list()

    # append vertex_b
    output.append(vertex_b)

    # walking backwards in "parent" dict
    while parent != vertex_a:
        output.append(parent)
        parent = dict_[parent]
    
    # prepending vertex_a
    output.append(vertex_a)
    output = output[::-1]
    
    print(f"Vertices in shortest path: {output}")
    print(f"Number of edges in shortest path: {len(output)-1}")
    
challenge_2("graph_data.txt", "1", "5")