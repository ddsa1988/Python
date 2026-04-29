for value in range(1, 5):
    print(value, end=" ")

print("\n")

for value in range(0, 11, 2):
    print(value, end=" ")

print("\n")

numbers = list(range(100, 120, 4))
print(numbers)
print()

magicians = ["alice", "david", "carolina"]

print("Magicians names: ", end=" ")

for index in range(len(magicians)):
    print(magicians[index], end=", ")
