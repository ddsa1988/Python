def main() -> None:
    numbers: list[int] = [10, 20, 30]

    print(numbers)

    numbers *= 3

    print(numbers)


if (__name__ == "__main__"):
    main()
