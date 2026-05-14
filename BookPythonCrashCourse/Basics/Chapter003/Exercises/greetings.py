def greeting(name: str) -> str:
    return f"Good morning {name}. How are doing?"


names: list[str] = ["Diego", "Amanda", "Amora", "Ameixa"]


print(greeting(names[0]))
print(greeting(names[1]))
print(greeting(names[2]))
print(greeting(names[3]))
