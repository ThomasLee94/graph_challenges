from classes.util.read_data import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse


def airplane_modelling(file_name: str, city_1: str, city_2: str) -> Graph:
    graph, verticies, edges_str = graph_from_file(file_name)

    # fill graph instance with edges and verticies
    fill(graph, verticies, edges_str)

    print(graph.vert_dict.keys())

    # most_connected_city = graph.find_max_influencer()
    # least_connected_city = graph.find_lonliest_vertex()
    # shortest_path = graph.min_weight_path(city_1, city_2)

    # print(f"The most connected city is: {most_connected_city}")
    # print(f"The least connected city is: {least_connected_city}")
    # print(
    #     f"The shortest path for a message between {city_1} & {city_2} is {shortest_path}"
    # )


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
        "city_1", help="instagram handle of 1st user", type=str
    )
    parser.add_argument(
        "city_2", help="instagram handle of 2nd user", type=str
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = cl_args()

    if not args.file_name:
        raise Exception("Text file was not provided!")
    if not args.city_1:
        raise Exception("A user was not provided!")
    if not args.city_2:
        raise Exception("A user was not provided!")

    airplane_modelling(args.file_name, args.city_1, args.city_2)

