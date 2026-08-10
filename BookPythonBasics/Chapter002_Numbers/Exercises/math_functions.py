def exercise001() -> None:
    decimal_places: int = 2
    number: float
    prompt: str = "Enter a number: "

    user_input: str = input(prompt)

    try:
        number = float(user_input)
    except:
        print("Invalid number.")
        return

    result: float = round(number, decimal_places)

    print(f"{number} rounded to {decimal_places} decimal places is {result}")


def exercise002() -> None:
    pass


def exercise003() -> None:
    pass


def main() -> None:
    exercise001()


if (__name__ == "__main__"):
    main()
