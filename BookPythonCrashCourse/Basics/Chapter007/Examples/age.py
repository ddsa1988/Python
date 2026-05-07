user_input = input("How old are you? ")

print(type(user_input))
print(isinstance(user_input, str))

try:
    age = int(user_input)
except ValueError:
    print("Invalid age.")

print(type(age))
print(isinstance(age, int))
