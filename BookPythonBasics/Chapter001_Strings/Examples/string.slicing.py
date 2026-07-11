def main() -> None:
    word: str = "apple pie"

    print(word[0:3])
    print(word[4:])
    print(word[:6])
    print(word[-3:-1])
    print("Empty string" if word[-3:0] == "" else word[-3:0])
    print(word[-3:])

    pass


if (__name__ == "__main__"):
    main()
