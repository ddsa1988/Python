# Default values
def describe_pet(pet_name: str, animal_type: str = "dog") -> None:
    print(f"I have an animal {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("harry")

print()

describe_pet("willie", "cat")
