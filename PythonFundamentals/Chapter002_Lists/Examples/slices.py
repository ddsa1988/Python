def main() -> None:
    spam: list[str] = ["cat", "bat", "rat", "elephant"]

    print(spam[0:3])
    print(spam[:3])
    print(spam[2:])
    print(spam[:])
    print(spam[-3:-1])


if (__name__ == "__main__"):
    main()
