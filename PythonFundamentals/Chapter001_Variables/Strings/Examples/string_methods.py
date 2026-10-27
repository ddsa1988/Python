def the_in_operator() -> None:
    text: str = "Hello World!"
    search: str = "World"

    print(search in text)
    print()


def changing_case() -> None:
    text: str = "Hello, world!"

    print(text.capitalize())
    print(text.upper())
    print(text.lower())
    print(text.title())
    print()


def check_string_characteristics() -> None:
    text: str = "diego"
    print(text.islower())
    print(text.isupper())
    print((text + "1988").isalnum())
    print("     ".isspace())
    print()


def check_start_end_string() -> None:
    text: str = "Hello World!"

    print(text.startswith("Hello"))
    print(text.endswith("?"))
    print()


def join_split_string() -> None:
    my_strings: list[str] = ["diego", "amanda", "amora", "eduarda", "ameixa"]
    print(", ".join(my_strings))

    text: str = """Dear Alice,
    There is a milk bottle in the fridge
    that is labeled "Milk Experiment."""

    text_split: list[str] = text.split("\n")  # type: ignore
    print(text_split)

    print()


def justify_and_centering() -> None:
    text: str = "Hello World!"

    print(text.rjust(20, "*"))
    print(text.ljust(20, "*"))
    print()


def remove_whitespace() -> None:
    text: str = "     Hello World     "

    print(text.lstrip())
    print(text.rstrip() + " *")
    print(text.strip())


def main() -> None:
    the_in_operator()
    changing_case()
    check_string_characteristics()
    check_start_end_string()
    join_split_string()
    justify_and_centering()
    remove_whitespace()


if (__name__ == "__main__"):
    main()
