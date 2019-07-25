from util.read_data import graph_from_file, string_to_tuple
from classes.digraph import Digraph

def challenge_3(file: str, vertex_a: str, vertex_b: str):
    _, verticies, edges_str = graph_from_file(file)
    
    # creating edge_list iterable 
    edge_list = list()
    for edge in edges_str:
        edge_list.append(string_to_tuple(edge))

    graph = Digraph()

    # add verticies
    for vertex in verticies:
        graph.add_vertex(vertex)
    
    # add edges and weights
    for tuple_ in edge_list:
        graph.add_edge(tuple_[0], tuple_[1], int(tuple_[2]))

    # using recursion, set used for dfs
    set_ = set()
    print(f"There exists a path between vertex {vertex_a} and {vertex_b}: {graph.dfs_recursive(vertex_a, vertex_b, set_, print)}")

challenge_3("graph_data.txt", "1", "5")