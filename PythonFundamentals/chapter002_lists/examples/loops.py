def main() -> None:
    spam: list[str] = ["cat", "bat", "rat", "elephant"]

    for item in spam:
        print(item, end=" ")

    print()

    for i in range(len(spam)):
        print(spam[i], end=" ")

    print()

    for index, item in enumerate(spam):
        print("Index " + str(index) + " : " + item)


if (__name__ == "__main__"):
    main()
