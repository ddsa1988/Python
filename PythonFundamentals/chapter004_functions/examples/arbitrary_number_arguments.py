def sum(*numbers: int) -> int:
    result: int = 0

    print(type(numbers))
    print(numbers)

    for value in numbers:
        result += value

    return result


def main() -> None:
    print(sum(10, 20, 30))

    print()

    print(sum(10, 20, 30, 40, 50))


if (__name__ == "__main__"):
    main()
