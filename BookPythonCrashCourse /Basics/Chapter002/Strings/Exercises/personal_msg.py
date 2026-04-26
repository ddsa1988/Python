name = "diego alexander"


def greeting(person_name: str) -> str:
    if type(person_name) is not str:
        return ""

    return f"Hello, {person_name.title()}. Have a nice day!"


print(greeting(name))
