def main() -> None:
    numbers: list[int] = [10, 20, 30, 40, 50]

    numbers.pop()

    print(numbers)

    numbers.pop(0)

    print(numbers)

    numbers.remove(30)

    print(numbers)


if (__name__ == "__main__"):
    main()
