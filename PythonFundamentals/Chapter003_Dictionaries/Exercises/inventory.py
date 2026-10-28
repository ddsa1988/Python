def display_inventory(items: dict[str, int]) -> None:
    raise NotImplementedError


def main() -> None:
    stuff: dict[str, int] = {'rope': 1, 'torch': 6,
                             'gold coin': 42, 'dagger': 1, 'arrow': 12}

    display_inventory(stuff)


if (__name__ == "__main__"):
    main()
