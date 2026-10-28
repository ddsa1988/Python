def main() -> None:
    spam: dict[str, str | int] = {"color": "red", "age": 42}

    print(spam.keys())
    print(spam.values())
    print(spam.items())
    print()

    for key in spam.keys():
        print(key)

    print()

    for value in spam.values():
        print(value)

    print()

    for key, value in spam.items():
        print(f"{key} = {value}")


if (__name__ == "__main__"):
    main()
