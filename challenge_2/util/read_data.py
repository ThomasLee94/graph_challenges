def graph_from_file(filepath):

    with open(filepath) as f:
        lines = f.read().splitlines()
        g_type, vertices, edges = lines[0], lines[1].split(','), lines[2:]

        return g_type, vertices, edges


def string_to_tuple(string):
    # Remove front and back parenthesis:
    string = string[1:-1]

    # Split by commas:
    elements = string.split(',')

    return tuple(elements)