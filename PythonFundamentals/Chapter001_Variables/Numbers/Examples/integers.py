def basic_of_integers():
    my_int: int = 10

    print(type(my_int))
    print(my_int)
    print()


def parse_string_to_int():
    my_number: int = int("50")

    print(type(my_number))
    print(my_number)
    print()


def main():
    basic_of_integers()
    parse_string_to_int()


if (__name__ == "__main__"):
    main()
