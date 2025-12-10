"""Module to read a text file and extract a graph of relations between characters."""


def read_txt(filename):
    """Reads a text file and returns its content as a string."""
    with open(filename, "r") as file:
        content = file.read()
    return content.split("\n\n")


def get_words_from_paragraph(paragraph):
    """Extracts words from a given paragraph."""
    words = paragraph.split()
    words = [word.strip(".,!?;:\"'()[]{}") for word in words]
    return words


if __name__ == "__main__":
    paragraphs = read_txt("devoir_4/book.txt")
    print(len(paragraphs), "paragraphs found in the book.")

    print(paragraphs[0])  # Print the first paragraph as a sample
    print(
        get_words_from_paragraph(paragraphs[0])
    )  # Print words from the first paragraph
    print(paragraphs[100:105])  # Print the last paragraph as a sample
    print(
        [words for words in map(get_words_from_paragraph, paragraphs[100:105])]
    )  # Print words from the last paragraph
