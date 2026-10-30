def basic_of_floats() -> None:
    my_float: float = 10.75

    print(type(my_float))
    print(my_float)
    print()


def parse_string_to_float() -> None:
    my_number: float = float("50.25")

    print(type(my_number))
    print(my_number)
    print()


def main() -> None:
    basic_of_floats()
    parse_string_to_float()


if (__name__ == "__main__"):
    main()
