def main() -> None:
    user_number: int
    user_input: str

    while (True):
        user_input = input("Type an integer number: ")

        try:
            user_number = int(user_input)
            break
        except ValueError:
            print("Invalid integer number.")

    if (user_number % 2 == 0):
        print(f"The number {user_number} is even.")
    else:
        print(f"The number {user_number} is odd.")


if (__name__ == "__main__"):
    main()
