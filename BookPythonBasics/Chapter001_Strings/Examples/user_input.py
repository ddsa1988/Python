def main() -> None:
    prompt: str = "Type something else: "

    user_input: str = input("Type something: ")
    print(f"You've typed: {user_input}")

    user_input = input(prompt)
    print(f"You've typed something else: {user_input}")


if (__name__ == "__main__"):
    main()
