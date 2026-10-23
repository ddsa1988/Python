def escape_characters():
    print("Say hi to Bob\'s mother")
    print("Hello there!\nHow are you?\nI'm doing\tfine.")
    print()


def raw_strings():
    print(r"The file is in C:\Users\Alice\Desktop")
    print()


def multiline_strings():
    print(""" Dear Alice,
    Can you feed the cat?
""")
    print()


def string_format():
    message: str = "Goof morning!"

    print(f"{message}")


def main():
    escape_characters()
    raw_strings()
    multiline_strings()
    string_format()


if (__name__ == "__main__"):
    main()
