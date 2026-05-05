user_0 = {
    "user_name": "efermi",
    "first_name": "enrico",
    "last_name": "fermi"
}

print(f"{user_0.items()}\n")
print(f"{user_0.keys()}\n")
print(f"{user_0.values()}\n")

for key, value in user_0.items():
    print(f"Key: {key}\nValue: {value}\n")

for key in user_0.keys():
    print(f"Key: {key}")

print()

for value in user_0.values():
    print(f"Value: {value}")

print()

for key in sorted(user_0.keys()):
    print(f"Key: {key}")
