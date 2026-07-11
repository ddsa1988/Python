def main() -> None:
    text1: str = "This multiline string is \
displayed on one line"

    text2: str = """This multiline string is 
displayed on two lines"""

    text3: str = """An example of a
        string that spans across multiple lines
            that also preserves whitespace."""

    print(text1 + "\n")
    print(text2 + "\n")
    print(text3)


if (__name__ == "__main__"):
    main()
