from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse

def challenge_3(file: str, vertex_a: str, vertex_b: str) -> Graph:
    graph_type, verticies, edges_str = graph_from_file(file)

    # Create graph depending on type
    if graph_type == "G":
        graph = Graph()
    if graph_type == "D":
        graph = Digraph()
    
    # fill graph instance with edges and verticies
    fill(graph, verticies, edges_str)

    # using recursion, set used for dfs
    set_ = set()
    list_ = graph.dfs_recursive(vertex_a, vertex_b, set_, print)
    print(f"There exists a path between vertex {vertex_a} and {vertex_b}: {list_[0]}")
    print(f"Vertices in the path: {list_[1]}")

challenge_3("graph_data_3.txt", "1", "5")