from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse


def instagram_modelling(file: str, user_1: str, user_2: str) -> Graph:
    graph, verticies, edges_str = graph_from_file(file)

    # fill graph instance with edges and verticies
    fill(graph, verticies, edges_str)

    influencer = graph.find_max_influencer()
    loner = graph.find_lonliest_vertex()
    message_shortest = graph.min_weight_path(user_1, user_2)


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
    parser.add_argument(
        "user_1", help="instagram handle of 1st user", type=str
    )
    parser.add_argument(
        "user_2", help="instagram handle of 2nd user", type=str
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = cl_args()

    if not args.file_name:
        raise Exception("Text file was not provided!")
    if not arge.user_1:
        raise Exception("A user was not provided!")
    if not arge.user_2:
        raise Exception("A user was not provided!")

    instagram_modelling(args.file_name, args.user_1, args.user_2)

