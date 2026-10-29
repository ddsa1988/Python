def add_to_inventory(inventory: dict[str, int], added_items: list[str]) -> None:
    for item in added_items:
        if (item in inventory):
            inventory[item] += 1
        else:
            inventory[item] = 1

        # inventory.setdefault(item, 0)
        # inventory[item] += 1


def display_inventory(inventory: dict[str, int]) -> None:
    print("Inventory:\n")

    number_of_items: int = 0

    for key, value in inventory.items():
        print(f"{key} = {value}")
        number_of_items += value

    print(f"\nTotal number of items: {number_of_items}")


def main() -> None:
    user_inventory: dict[str, int] = {"gold coin": 42, "rope": 1}

    dragon_loot: list[str] = ['gold coin',
                              'dagger', 'gold coin', 'gold coin', 'ruby']

    add_to_inventory(user_inventory, dragon_loot)
    display_inventory(user_inventory)


if (__name__ == "__main__"):
    main()
