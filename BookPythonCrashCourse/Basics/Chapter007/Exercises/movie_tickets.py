is_active: bool = True

print("***** Welcome to the movie tickets ****\n")

while (is_active):
    user_age: int = 0
    user_input: str = input(
        "How old are you? Type your age or 'quit' to exit: ")

    if (user_input.lower().strip() == "quit"):
        break

    try:
        user_age = int(user_input)

        if (user_age < 0):
            raise ValueError("Age must be a positive number.")

    except ValueError:
        print("Invalid age.")
        continue

    if (user_age < 3):
        print("The ticket is free.")
        continue

    if (user_age >= 3 and user_age < 12):
        print("The ticket costs R$10")
        continue

    print("The ticket costs R$15")
