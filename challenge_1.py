from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse

def challenge_1(file: str) -> Graph:
    graph, verticies, edges_str = graph_from_file(file)
    
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

def cl_args() -> argparse.Namespace:
    """
        function to execute command line arguments

        Returns
            parsed objects 
    """

    parser = argparse.ArgumentParser(description="Create graph from text file!")
    parser.add_argument("file_name", help="Name of data in text file")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = cl_args()

    if not args.file_name:
        raise Exception("Text file was not provided!")
    challenge_1(args.file_name)