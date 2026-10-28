def display_inventory(inventory: dict[str, int]) -> None:
    print("Inventory:\n")

    number_of_items: int = 0

    for key, value in inventory.items():
        print(f"{key} = {value}")
        number_of_items += value

    print(f"\nTotal number of items: {number_of_items}")


def main() -> None:
    stuff: dict[str, int] = {'rope': 1, 'torch': 6,
                             'gold coin': 42, 'dagger': 1, 'arrow': 12}

    display_inventory(stuff)


if (__name__ == "__main__"):
    main()
