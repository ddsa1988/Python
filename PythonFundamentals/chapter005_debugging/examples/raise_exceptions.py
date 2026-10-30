def create_user(first_name: str, last_name: str) -> dict[str, str]:
    if (type(first_name) != str):
        raise TypeError("First name must be a string.")

    if (len(first_name.strip()) == 0):
        raise ValueError("First name must not be empty.")

    if (type(last_name) != str):
        raise TypeError("First name must be a string.")

    if (len(last_name.strip()) == 0):
        raise ValueError("First name must not be empty.")

    user: dict[str, str] = {
        "first_name": first_name.title(),
        "last_name": last_name.title()
    }

    return user


def main() -> None:
    try:
        create_user(" ", "alexander")
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


if (__name__ == "__main__"):
    main()
