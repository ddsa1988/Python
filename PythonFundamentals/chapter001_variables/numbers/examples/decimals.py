from decimal import Decimal


def decimals() -> None:
    my_decimal: Decimal = Decimal("10.75")

    print(type(my_decimal))
    print(my_decimal)
    print()


def parse_string_to_decimal() -> None:
    my_number: Decimal = Decimal("50.25")

    print(type(my_number))
    print(my_number)
    print()


def main() -> None:
    decimals()
    parse_string_to_decimal()


if (__name__ == "__main__"):
    main()
