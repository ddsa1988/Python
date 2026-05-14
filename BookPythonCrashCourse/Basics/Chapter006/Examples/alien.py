alien_0: dict[str, any] = {"color": "green", "points": 5}

print(f"{alien_0}\n")

print(f"color: {alien_0['color']}\n")

print(f"points: {alien_0['points']}\n")

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(f"{alien_0}\n")

alien_0["color"] = "red"

print(f"{alien_0}\n")

del alien_0["points"]

print(f"{alien_0}\n")
