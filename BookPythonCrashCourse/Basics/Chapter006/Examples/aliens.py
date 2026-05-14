alien_0: dict[str, any] = {"color": "green", "points": 5}
alien_1: dict[str, any] = {"color": "yellow", "points": 10}
alien_2: dict[str, any] = {"color": "red", "points": 15}

aliens: list[dict[str, any]] = [alien_0, alien_1, alien_2]

print(f"{aliens}\n")

print(f"Length: {len(aliens)}\n")

for alien in aliens:
    print(f"{alien}\n")
