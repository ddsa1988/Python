def main() -> None:
    text: str = "This is a paragraph. And this is another paragraph."
    string_searched: str = "this"

    print(text.find(string_searched))
    print(text.lower().find(string_searched))
    print(text.upper().find(string_searched))


if (__name__ == "__main__"):
    main()
