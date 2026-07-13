def main() -> None:
    leet_speak: dict[str, str] = {
        "a": "4",
        "b": "8",
        "e": "3",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7",
    }

    prompt: str = "Enter some text: "
    user_input: str = input(prompt)

    if (len(user_input) == 0):
        return

    output: str = user_input.capitalize()

    for key, value in leet_speak.items():
        if (key not in output):
            continue

        output = output.replace(key, value)

    print(output)


if (__name__ == "__main__"):
    main()
