def greeting(person_name: str) -> str:
    if type(person_name) != str:
        return ""

    return f"Hello, {person_name.title()}. Have a nice day!"


name = "diego alexander"

print(greeting(name))
