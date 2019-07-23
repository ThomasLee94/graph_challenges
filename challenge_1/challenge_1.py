from util.read_data import graph_from_file, string_to_tuple
from classes.vertex import Vertex
from classes.digraph import Digraph

def challenge_1(file: str) -> str:
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
    
    # print vertices
    print(f"Verticies: {len(graph.get_vertices())}")
    
    # print edges
    print(f"Edges: {graph.num_edges}")
   
    # print edge list
    for vertex in graph.vert_dict:
        vert = graph.get_vertex(vertex) 
        for neighbour, weight in vert.adj_dict_neighbours.items():
            print(f"({vert.id}, {neighbour.id}, {weight})")

challenge_1("graph_data.txt")