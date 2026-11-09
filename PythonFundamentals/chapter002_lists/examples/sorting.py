def main() -> None:
    numbers: list[int] = [30, 10, 20]

    print(sorted(numbers))

    numbers.sort()

    print(numbers)


if (__name__ == "__main__"):
    main()
