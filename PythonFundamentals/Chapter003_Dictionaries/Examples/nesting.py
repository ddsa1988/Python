def dictionary_inside_list() -> None:
    users: list[dict[str, str]] = [
        {
            "first": "diego",
            "last": "alexander",
            "location": "brazil"
        },
        {
            "first": "amanda",
            "last": "perna",
            "location": "france"
        }]

    for user in users:
        print(user)

    print()


def list_inside_dictionary() -> None:
    users: dict[str, list[str]] = {
        "diego": ["diego", "alexander", "brazil"],
        "amanda": ["amanda", "perna", "france"]
    }

    for key, value in users.items():
        print(f"{key} = {value}")

    print()


def dictionary_inside_dictionary() -> None:
    users: dict[str, dict[str, str]] = {
        "diego": {
            "first": "diego",
            "last": "alexander",
            "location": "brazil"
        },
        "amanda": {
            "first": "amanda",
            "last": "perna",
            "location": "france"
        }
    }

    for key, value in users.items():
        print(f"{key} : {value}")

    print()


def main() -> None:
    dictionary_inside_list()
    list_inside_dictionary()
    dictionary_inside_dictionary()


if (__name__ == "__main__"):
    main()
