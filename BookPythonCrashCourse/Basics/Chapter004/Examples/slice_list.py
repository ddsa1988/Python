# Slice => [start, stop, step]

players: list[str] = ["charles", "martina", "michael", "florence", "eli"]
numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(players[1:3])
print(players[:3])
print(players[1:4])
print(players[1:])
print(players[-3:])
print(players[-3:-1])

print(numbers[0:len(numbers):2])
