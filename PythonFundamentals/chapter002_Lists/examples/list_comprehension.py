def main() -> None:
    spam: list[str] = ["cat", "bat", "rat", "elephant"]

    squares: list[int] = [value ** 2 for value in range(10)]

    spam_upper: list[str] = [item.upper() for item in spam]

    print(squares)
    print(spam_upper)


if (__name__ == "__main__"):
    main()
