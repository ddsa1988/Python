def main() -> None:
    spam: list[str] = ["cat", "bat", "rat", "elephant"]

    print(str(spam) + "\n")

    print(spam[0])  # First index
    print(spam[len(spam) - 1])  # Last index
    print()

    print(spam[len(spam) * - 1])  # First index
    print(spam[-1])  # Last index


if (__name__ == "__main__"):
    main()
