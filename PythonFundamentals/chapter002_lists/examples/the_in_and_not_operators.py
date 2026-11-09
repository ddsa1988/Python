def main() -> None:
    spam: list[str] = ["cat", "bat", "rat", "elephant"]

    if ("cat" in spam):
        print("Nice")

    if ("dog" not in spam):
        print("Cool")


if (__name__ == "__main__"):
    main()
