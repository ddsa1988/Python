def main() -> None:
    word: str = "Python"

    for letter in word:
        print(letter, end=", ")

    print()

    for number in range(10):
        print(number, end=" ")

    print()

    for number in range(1, 20, 2):
        print(number, end=" ")

    print()

    for index in range(len(word)):
        print(word[index], end=" ")


if (__name__ == "__main__"):
    main()
