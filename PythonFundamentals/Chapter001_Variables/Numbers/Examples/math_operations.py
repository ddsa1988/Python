def subtraction() -> None:
    my_int_1: int = 10
    my_int_2: int = 15

    my_float_1: float = 52.75
    my_float_2: float = 74.63

    print("***** Subtraction *****")
    print(my_int_2 - my_int_1)
    print(my_float_2 - my_float_1)
    print()


def addition() -> None:
    my_int_1: int = 10
    my_int_2: int = 15

    my_float_1: float = 52.75
    my_float_2: float = 74.63

    print("***** Addition *****")
    print(my_int_2 + my_int_1)
    print(my_float_2 + my_float_1)
    print()


def multiplication() -> None:
    my_int_1: int = 10
    my_int_2: int = 15

    my_float_1: float = 52.75
    my_float_2: float = 74.63

    print("***** Multiplication *****")
    print(my_int_2 * my_int_1)
    print(my_float_2 * my_float_1)
    print()


def division() -> None:
    my_int_1: int = 10
    my_int_2: int = 15

    my_float_1: float = 52.75
    my_float_2: float = 74.63

    print("***** Division *****")
    print(my_int_2 // my_int_1)  # Integer division
    print(my_int_2 / my_int_1)  # Float division
    print(my_float_2 / my_float_1)
    print()


def main():
    subtraction()
    addition()
    multiplication()
    division()


if (__name__ == "__main__"):
    main()
