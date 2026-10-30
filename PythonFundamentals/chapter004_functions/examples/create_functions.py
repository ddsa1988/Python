def greet_user_1() -> None:
    print("Hello!")


def greet_user_2(name: str) -> None:
    print(f"Hello, {name.title()}!")


def greet_user_3(name: str, msg: str = "Hello") -> None:
    print(f"{msg}, {name.title()}!")


def get_formatted_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}".title()


def build_person(first_name: str, last_name: str, age: int | None = None) -> dict[str, str | int]:
    person: dict[str, str | int] = {
        'first name': first_name, "last name": last_name}

    if (age != None):
        person["age"] = age

    return person


def main() -> None:
    greet_user_1()
    greet_user_2(name="diego")
    greet_user_3(name="diego")
    greet_user_3(name="diego", msg="Good morning")

    print(get_formatted_name("diego", "alexander"))
    print(build_person("diego", "alexander"))
    print(build_person("diego", "alexander", 38))


if (__name__ == "__main__"):
    main()
