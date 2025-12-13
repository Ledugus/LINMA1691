"""Module to read a text file and extract a graph of relations between characters."""

from nickname_list import NICKNAMES
import numpy as np
import pandas as pd


def process_nicknames(nicknames):
    """Processes nicknames to create a mapping from nickname to character index."""
    nickname_to_index = []
    for index, names in enumerate(nicknames):
        names.sort(key=len, reverse=True)
        for name in names:
            nickname_to_index.append([name, index])
    nickname_to_index = sorted(nickname_to_index, key=lambda x: -len(x[0]))
    return nickname_to_index


def read_txt(filename):
    """Reads a text file and returns its content as a list of paragraphs."""
    with open(filename, "r") as file:
        content = file.read()
    return content.split("\n\n")


def process_paragraph(paragraph, nickname_list):
    """Processes a paragraph to extract cluster of characters."""
    cluster = []
    for nickname, index in nickname_list:
        if nickname in paragraph:
            cluster.append(index)
    return cluster


def adj_from_clusters(clusters):
    """Generates a graph of relations from clusters of characters."""

    adj = np.zeros((len(NICKNAMES), len(NICKNAMES)), dtype=int)
    for cluster in clusters:
        unique_characters = set(cluster)
        unique_characters = list(unique_characters)
        for character in unique_characters:
            adj[character, unique_characters] += 1
            adj[character, character] -= 1
    return adj


def edges_from_clusters(clusters):
    """Generates edges from clusters of characters."""
    edges = []
    for cluster in clusters:
        unique_characters = set(cluster)
        unique_characters = list(unique_characters)
        unique_characters.sort()
        for i, character1 in enumerate(unique_characters):
            for character2 in unique_characters[i + 1 :]:
                edges.append([character1, character2])
    return edges


def nodes_from_nicknames():
    """Generates nodes from nicknames."""
    ids = []
    names = []
    for index, person_nicknames in enumerate(NICKNAMES):
        ids.append(index)
        names.append(person_nicknames[0])

    df = pd.DataFrame({"Id": ids, "Label": names})
    df.to_csv("devoir_4/nodes.csv", sep=";", index=False)


if __name__ == "__main__":
    paragraphs = read_txt("devoir_4/book.txt")
    print(len(paragraphs), "paragraphs found in the book.")

    nickname_dict = process_nicknames(NICKNAMES)
    print(len(nickname_dict), "nicknames processed.")
    print(nickname_dict)
    clusters = [process_paragraph(paragraph, nickname_dict) for paragraph in paragraphs]

    edge_list = np.array(edges_from_clusters(clusters))
    print(len(edge_list), "edges found in the book.")

    nodes_from_nicknames()
    np.savetxt("devoir_4/edge_list.csv", edge_list, delimiter=";", fmt="%d")

    adj = adj_from_clusters(clusters)
    np.savetxt("devoir_4/adjacency_matrix.csv", adj, delimiter=";", fmt="%d")
