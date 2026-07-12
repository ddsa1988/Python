def main() -> None:
    text: str = "This is some text."

    print(text.startswith("This"))
    print(text.startswith("this"))

    print(text.endswith("text."))
    print(text.endswith("Text."))


if (__name__ == "__main__"):
    main()
