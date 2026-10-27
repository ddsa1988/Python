def main() -> None:
    numbers: list[int] = [10, 20, 30]

    print(numbers)

    del numbers[1]

    print(numbers)


if (__name__ == "__main__"):
    main()
