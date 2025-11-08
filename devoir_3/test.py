from pathfinder_hw import eulerian_path_finder

"""
Loads the graph contained in file.
"""


def load_graph(file_name):
    graph = []
    with open(file_name, "r") as file:
        txt = file.read().split("\n")
        for line in txt[1:-1]:
            adj = []
            for node in line.split(","):
                adj.append(int(node))
            graph.append(adj)
        while len(graph) != int(txt[0]):
            graph.append([])
    return graph


"""
Translate a graph from adjacency list to file representation.
"""


def from_adj_to_str(graph):
    output = str(len(graph))
    for line in graph:
        output += "\n"
        for adj in line:
            output += str(adj) + ","
        output = output[:-1]
    output += "\n"
    return output


"""
Writes a graph into file_name.
"""


def save_graph(file_name, graph):
    with open(file_name, "w") as file:
        file.write(from_adj_to_str(graph))


def count_edges(graph):
    count = 0
    for node in graph:
        count += len(node)
    return count / 2


def validate_path(graph, path):
    if path is None:
        return False
    temp_graph = [adj.copy() for adj in graph]
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        if v in temp_graph[u]:
            temp_graph[u].remove(v)
            temp_graph[v].remove(u)
        else:
            return False
    for adj in temp_graph:
        if adj:
            return False
    return True


if __name__ == "__main__":
    for i in range(1, 5):

        graph = load_graph(f"test_0{i}.txt")
        path = eulerian_path_finder(graph)
        print(
            f"Test N°{i} :",
            validate_path(graph, path),
            "with path length",
            len(path) if path else 0,
            "and edge count",
            int(count_edges(graph)),
            f"(path : {path})",
        )
        save_graph(f"test_0{i}.txt", graph)
