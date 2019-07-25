from classes.digraph import Digraph
from classes.graph import Graph
from classes.vertex import Vertex

def graph_from_file(filepath):
	""" 
		Opens a text file and returns:
			g_type: graph type 
			verticies:
			edges: 
	"""

	with open(filepath) as f:
		lines = f.read().splitlines()
		g_type, vertices, edges = lines[0], lines[1].split(','), lines[2:]

	return g_type, vertices, edges


def string_to_tuple(string):
	"""
		turns a string into a tuple 
	"""
    # Remove front and back parenthesis:
	string = string[1:-1]

    # Split by commas:
	elements = string.split(',')

	return tuple(elements)