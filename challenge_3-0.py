from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse


def challenge_3(file: str, vertex_a: str, vertex_b: str) -> Graph:
    graph, verticies, edges_str = graph_from_file(file)

    # fill graph instance with edges and verticies
    fill(graph, verticies, edges_str)

    # using recursion, set used for dfs
    set_ = set()
    visited_list = list()
    tuple_ = graph.dfs_recursive(vertex_a, vertex_b, visited_list, set_, print)
    print(
        f"There exists a path between vertex {vertex_a} and {vertex_b}: {tuple_[0]}"
    )
    print(f"Vertices in the path: {tuple_[1]}")


def cl_args() -> argparse.Namespace:
    """
        function to execute command line arguments

        Returns
            parsed objects 
    """

    parser = argparse.ArgumentParser(
        description="Create graph from text file!"
    )
    parser.add_argument(
        "file_name", help="Name of data in text file", type=str
    )
    parser.add_argument("vertex_a", help="start vertex", type=str)
    parser.add_argument("vertex_b", help="end vertex", type=str)
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = cl_args()

    if not args.file_name:
        raise Exception("Text file was not provided!")

    if not args.vertex_a:
        raise Exception("Start vertex was not provided!")

    if not args.vertex_b:
        raise Exception("End vertex was not provided!")

    challenge_3(args.file_name, args.vertex_a, args.vertex_b)

