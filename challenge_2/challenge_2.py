from read_data import graph_from_file, string_to_tuple
from vertex import Vertex
from graph import Graph

def challenge_2():
    _, verticies, edges_str = graph_from_file("graph_data.txt")
    
    # creating edge_list iterable 
    edge_list = list()
    for edge in edges_str:
        edge_list.append(string_to_tuple(edge))

    graph = Graph()

    # add verticies
    for vertex in verticies:
        graph.add_vertex(vertex)
    
    # add edges
    for tuple_ in edge_list:
        graph.add_edge(tuple_[0], tuple_[1])
    
    output = graph.breadth_first_search("1","5")
    edges = graph.get_edges("1")

    # print(graph.vert_dict)
    print(verticies)
    print(edge_list)
    print(f"EDGES: {edges}")

challenge_2()