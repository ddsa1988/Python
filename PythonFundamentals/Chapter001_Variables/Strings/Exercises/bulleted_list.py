def split_text(text: str, separator: str) -> list[str]:
    if (type(text) != str):
        raise TypeError("Text must be a string type.")

    if (type(separator) != str):
        raise TypeError("Separator must be a string type")

    new_list: list[str] = text.split(separator)

    return new_list


def add_bullet(word: str) -> str:
    new_word: str = "*" + " " + word

    return new_word


def main():
    content: str = """Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars"""

    lines: list[str] = split_text(text=content, separator="\n")

    new_lines: list[str] = [
        add_bullet(word=item) for item in lines]  # List Comprehension

    print("\n".join(new_lines))


if (__name__ == "__main__"):
    main()
