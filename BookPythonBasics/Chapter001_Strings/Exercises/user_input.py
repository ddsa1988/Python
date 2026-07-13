def main() -> None:
    user_input: str = input("Type something: ")
    result: str = user_input.strip().lower()

    print(
        f"You've typed: '{result}' and it has {len(result)} letters.")


if (__name__ == "__main__"):
    main()
