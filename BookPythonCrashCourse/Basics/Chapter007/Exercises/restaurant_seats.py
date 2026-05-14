user_input: str = input("How many people are in your dinner group? ")

try:
    guests_number: int = int(user_input)

    if (guests_number > 8):
        print("Your group have to wait for a table.")
    else:
        print("Your table is ready.")

except ValueError:
    print("Invalid number.")
