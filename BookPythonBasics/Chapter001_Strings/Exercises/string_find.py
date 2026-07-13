def main() -> None:
    text: str = "This is a paragraph. And this is another paragraph. And this is the last paragraph."
    string_searched: str = "paragraph"
    last_index: int = 0
    actual_index: int = 0
    results: list[str] = []

    while (True):
        actual_index = text.find(string_searched, last_index)

        if (actual_index == -1):
            break

        results.append(text[last_index:actual_index].strip())
        last_index = actual_index + len(string_searched)

    print(results)


if (__name__ == "__main__"):
    main()
