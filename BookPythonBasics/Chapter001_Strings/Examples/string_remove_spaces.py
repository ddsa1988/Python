def main() -> None:
    text: str = "    Hello    "
    someText: str = " World."
    print(text + someText)

    print(text.rstrip() + someText)
    print(text.lstrip() + someText)
    print(text.strip() + someText)


if (__name__ == "__main__"):
    main()
