from collections.abc import Callable

# lambda argument(s) : expression


def main() -> None:
    square: Callable[[int], int] = lambda x: x ** 2

    print(square(2))
    print(square(3))


if (__name__ == "__main__"):
    main()
