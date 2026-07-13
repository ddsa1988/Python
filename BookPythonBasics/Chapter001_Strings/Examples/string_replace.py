def main() -> None:
    text: str = "This is a paragraph. And this is another paragraph."

    print(text.lower().replace("this", "***"))


if (__name__ == "__main__"):
    main()
