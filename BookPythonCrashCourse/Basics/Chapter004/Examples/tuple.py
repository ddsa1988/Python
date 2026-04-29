# Tuples cannot change the items values

names = ("diego", "amanda", "eduarda")
print(names)

print()

try:
    names[0] = "Amora"
except TypeError:
    print("Tuple does not support item assignment")

print()

for name in names:
    print(name, end=" ")
