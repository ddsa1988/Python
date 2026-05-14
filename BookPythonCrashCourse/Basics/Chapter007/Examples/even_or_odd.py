user_input: str = input(
    "Enter a number, and I'll tell you if it's even or odd: ")

try:
    number: int = int(user_input)

    if (number % 2 == 0):
        print(f"The number {number} is even.")
    else:
        print(
            f"The number {number} is odd.")

except ValueError:
    print("Invalid number.")
