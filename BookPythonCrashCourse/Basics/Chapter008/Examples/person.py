from datetime import date


def build_person(first_name: str, last_name: str, birthdate: date | None = None) -> dict[str, str]:
    person: dict[str, str] = {}

    if (len(first_name.strip()) == 0 or len(last_name.strip()) == 0):
        return {}

    person["first_name"] = first_name.title()
    person["last_name"] = last_name.title()

    if (type(birthdate) == date):
        person["birthdate"] = str(birthdate)

    return person


person1: dict[str, str] = build_person("diego", "alexandre")
person2: dict[str, str] = build_person("diego", "alexandre", date(1988, 1, 22))

print(f"{person1}\n")
print(f"{person2}\n")
