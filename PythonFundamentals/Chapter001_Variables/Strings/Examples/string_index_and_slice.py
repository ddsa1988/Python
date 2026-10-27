def indexes() -> None:
    full_name: str = "Diego dos Santos Alexander"

    print(full_name[0])
    print(full_name[4])

    print(full_name[-1])
    print(full_name[-4])

    print(full_name[len(full_name) - 1])
    print()


def slicing() -> None:
    full_name: str = "Diego dos Santos Alexander"

    first_name: str = full_name[0:5]
    print(first_name)

    last_name: str = full_name[-9:]
    print(last_name)

    print(full_name[:])


def main() -> None:
    indexes()
    slicing()


if (__name__ == "__main__"):
    main()
