from util.read_data import graph_from_file, string_to_tuple
from classes.vertex import Vertex
from classes.graph import Graph

def challenge_2(file: str, vertex_a: str, vertex_b: str)->str:
    _, verticies, edges_str = graph_from_file(file)
    
    # creating edge_list iterable 
    edge_list = list()
    for edge in edges_str:
        edge_list.append(string_to_tuple(edge))

    # create graph
    graph = Graph()

    # add verticies
    for vertex in verticies:
        graph.add_vertex(vertex)
    
    # add edges
    for tuple_ in edge_list:
        graph.add_edge(tuple_[0], tuple_[1])
    
    # getting parent dict
    dict_ = graph.breadth_first_search(vertex_a,vertex_b)

    parent = dict_[vertex_b]
    output = list()

    # append vertex_b
    output.append(vertex_b)

    # walking backwards in "parent" dict
    while parent != vertex_a:
        output.insert(0, parent)
        parent = dict_[parent]
    
    # prepending vertex_a
    output.insert(0, vertex_a)

    print(f"Vertices in shortest path: {output}")
    print(f"Number of edges in shortest path: {len(output)-1}")
    
challenge_2("graph_data.txt", "1", "5")