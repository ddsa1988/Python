def main() -> None:
    my_cat: dict[str, str | int] = {
        "size": "fat",
        "color": "gray",
        "age": 17
    }

    my_cat["breed"] = "unknown"

    my_cat.setdefault("address", "brazil")

    print(my_cat)


if (__name__ == "__main__"):
    main()
