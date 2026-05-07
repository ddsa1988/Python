pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
pet_to_be_removed = "cat"

print(f"{pets}\n")

while (pet_to_be_removed in pets):
    pets.remove(pet_to_be_removed)

print(pets)
