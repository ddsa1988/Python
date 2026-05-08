def describe_pet(animal_type: str, pet_name: str) -> None:
    print(f"I have an animal {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Positional arguments
describe_pet("hamster", "harry")

print()

# keyword arguments
describe_pet(pet_name="willie", animal_type="dog")
