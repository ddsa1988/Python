def changing_case():
    text: str = "Hello, world!"

    print(text.capitalize())
    print(text.upper())
    print(text.lower())
    print(text.title())
    print()


def check_string_characteristics():
    print("diego".islower())
    print("diego.".isupper())
    print("diego1988".isalnum())
    print("     ".isspace())
    print()


def check_start_end_string():
    pass


def main():
    changing_case()
    check_string_characteristics()


if (__name__ == "__main__"):
    main()
