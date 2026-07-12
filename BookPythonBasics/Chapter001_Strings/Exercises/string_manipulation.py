def exercise001() -> None:
    words: list[str] = ["Animals", "Badger", "Honey Bee", "Honey badger"]

    print("Words to lower case:")

    for word in words:
        print(word.lower())


def exercise002() -> None:
    words: list[str] = ["Animals", "Badger", "Honey Bee", "Honey badger"]

    print("Words to upper case:")

    for word in words:
        print(word.upper())


def exercise003() -> None:
    words: list[str] = ["    Filet Mignon",
                        "Brisket    ", "    Cheeseburger    "]

    print("Remove words whitespace:")

    for word in words:
        print(word.strip())


def exercise004() -> None:
    words: list[str] = ["Becomes", "becomes", "BEAR", "    bEautiful"]
    searchWord = "be"

    print(f"Words that start with {searchWord}:")

    for word in words:
        print(f"{word} -> {word.startswith(searchWord)}")


def exercise005() -> None:
    words: list[str] = ["Becomes", "becomes", "BEAR", "    bEautiful"]
    searchWord = "be"

    print(f"Words that start with {searchWord}:")

    for word in words:
        changedWord = word.strip().lower()

        print(f"{changedWord} -> {changedWord.startswith(searchWord)}")


def main() -> None:
    exercise001()
    print()
    exercise002()
    print()
    exercise003()
    print()
    exercise004()
    print()
    exercise005()


if (__name__ == "__main__"):
    main()
