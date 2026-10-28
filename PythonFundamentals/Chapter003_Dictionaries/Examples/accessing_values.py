def main() -> None:
    my_cat: dict[str, str | int] = {
        "size": "fat",
        "color": "gray",
        "age": 17
    }

    print(my_cat)
    print(my_cat["size"])
    print(my_cat.get("age"))
    print(my_cat.get("test", "default"))

    try:
        print(my_cat["test"])
    except KeyError:
        print("Key not found.")


if (__name__ == "__main__"):
    main()
