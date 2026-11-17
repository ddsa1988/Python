from functools import reduce


def main() -> None:
    numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    numbers_squares: list[int] = list(map(lambda x: x ** 2, numbers))  # noqa: C417
    numbers_evens: list[int] = list(filter(lambda x: x % 2 == 0, numbers))
    numbers_sum: int = reduce(lambda x, y: x + y, numbers)

    print("Original: " + str(numbers))
    print("Squares:" + str(numbers_squares))
    print("Evens: " + str(numbers_evens))
    print("Sum: " + str(numbers_sum))


if (__name__ == "__main__"):
    main()
