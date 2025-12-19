import networkx as nx
from networkx.drawing.layout import forceatlas2_layout
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
import pandas as pd


def get_graph_from_edge_list(edge_list):

    edge_list = pd.read_csv(edge_list, sep=";", header=None).values.tolist()
    edge_list = [tuple(sorted(edge)) for edge in edge_list]
    edge_list_unique = list(set(edge_list))
    weights = [edge_list.count(edge) for edge in edge_list_unique]
    final_edges = []
    for i in range(len(edge_list_unique)):
        final_edges.append((edge_list_unique[i][0], edge_list_unique[i][1], weights[i]))
    G = nx.Graph()
    G.add_weighted_edges_from(final_edges)
    return G


def plot_graph(
    G,
    figsize=(10, 10),
    node_size=100,
    edge_width=0.5,
    node_color="skyblue",
    font_size=8,
):
    pos = forceatlas2_layout(G, scaling_ratio=200, gravity=0.2, max_iter=1000)
    weights = [G[u][v]["weight"] for u, v in G.edges()]
    widths = [edge_width * w for w in weights]
    plt.figure(figsize=figsize)

    nx.draw_networkx_nodes(
        G, pos, node_size=node_size, node_color=node_color, alpha=0.7
    )
    nx.draw_networkx_edges(G, pos, width=widths, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=font_size, font_color="black")

    plt.show()


if __name__ == "__main__":
    G = get_graph_from_edge_list("devoir_4/edge_list.csv")
    partitions = list(
        nx.community.greedy_modularity_communities(G, weight="weight", resolution=1)
    )
    color_map = plt.get_cmap("tab20", len(partitions))
    group_to_color = {i: colors.to_hex(color_map(i)) for i, g in enumerate(partitions)}
    print(group_to_color)
    print(partitions)
    node_color = [0] * G.number_of_nodes()
    for i, partition in enumerate(partitions):
        for node in partition:
            node_color[node] = group_to_color[i]
    plot_graph(G, edge_width=0.2, node_size=200, font_size=6, node_color=node_color)
