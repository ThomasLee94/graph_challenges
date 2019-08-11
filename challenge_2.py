from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse


def challenge_2(file: str, vertex_a: str, vertex_b: str) -> Graph:
    graph, verticies, edges_str = graph_from_file(file)

    # fill graph instance with edges and verticies
    fill(graph, verticies, edges_str)

    # getting parent dict
    dict_ = graph.breadth_first_search(vertex_a, vertex_b)

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


def cl_args() -> argparse.Namespace:
    """
        function to execute command line arguments

        Returns
            parsed objects
    """

    parser = argparse.ArgumentParser(description="Create graph from text file")
    parser.add_argument("file_name", help="text data file", type=str)
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

    challenge_2(args.file_name, args.vertex_a, args.vertex_b)
