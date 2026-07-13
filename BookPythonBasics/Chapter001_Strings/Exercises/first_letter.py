def main() -> None:
    user_input: str = input("Tell me your password: ").strip()

    if (len(user_input) == 0):
        return

    first_letter: str = user_input[0]

    print(f"The first letter you entered was: {first_letter.upper()}")


if (__name__ == "__main__"):
    main()
