def exercise_001() -> None:
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

    print(f"{number} rounded to {decimal_places} decimal places is {result}.")


def exercise_002() -> None:
    number: float

    prompt: str = "Enter a negative number: "
    user_input: str = input(prompt)

    try:
        number = float(user_input)
    except:
        print("Invalid number.")
        return

    result: float = abs(number)

    print(f"The absolute value of {number} is {result}.")


def exercise_003() -> None:
    number_1: float
    number_2: float

    prompt: str = "Enter the first number: "
    user_input: str = input(prompt)

    try:
        number_1 = float(user_input)
    except:
        print("Invalid number.")
        return

    prompt = "Enter the second number: "
    user_input = input(prompt)

    try:
        number_2 = float(user_input)
    except:
        print("Invalid number.")
        return

    result: bool = (number_1 - number_2).is_integer()

    print(
        f"The difference between {number_1} and {number_2} is an integer? {result}.")


def main() -> None:
    exercise_001()
    print()

    exercise_002()
    print()

    exercise_003()
    print()


if (__name__ == "__main__"):
    main()
