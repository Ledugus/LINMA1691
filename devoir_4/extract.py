import numpy as np
import pandas as pd


def load_character_info():
    """Loads nicknames from a text file."""
    characters = pd.read_csv("devoir_4/character_info.csv", sep=";")
    characters["Names"] = characters["Names"].apply(lambda x: x.split(", "))
    return characters


def read_txt(filename):
    """Reads a text file and returns its content as a list of paragraphs."""
    with open(filename, "r") as file:
        content = file.read()

    paragraphs = content.split("\n\n")
    merged_paragraphs = []

    current_paragraph = ""
    for paragraph in paragraphs:
        if len(paragraph) < 1:
            continue
        if paragraph[0] == "“":
            current_paragraph += " " + paragraph
        else:
            merged_paragraphs.append(current_paragraph)
            current_paragraph = paragraph
    return merged_paragraphs


def process_paragraph(paragraph, characters):
    """Processes a paragraph to extract cluster of characters."""
    cluster = []
    for index, nicknames in enumerate(characters["Names"]):
        for nickname in nicknames:
            if nickname in paragraph:
                cluster.append(index)
    print(cluster)
    return cluster


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


if __name__ == "__main__":
    paragraphs = read_txt("devoir_4/book.txt")
    characters_df = load_character_info()
    clusters = [process_paragraph(paragraph, characters_df) for paragraph in paragraphs]

    edge_list = np.array(edges_from_clusters(clusters))
    print(len(edge_list), "edges found in the book.")

    np.savetxt("devoir_4/edge_list.csv", edge_list, delimiter=";", fmt="%d")
