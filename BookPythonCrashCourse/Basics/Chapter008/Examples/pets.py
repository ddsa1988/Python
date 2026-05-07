def describe_pet(animal_type: str, pet_name: str) -> None:
    print(f"I have an animal {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")
