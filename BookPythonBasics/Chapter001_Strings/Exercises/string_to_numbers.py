def exercise_001() -> None:
    my_string: str = "18.75"
    my_multiplier: int = 2
    my_number: float = float(my_string)

    if (type(my_number) == float):
        print(f"{my_number} * {my_multiplier} -> {my_number * my_multiplier}")


def exercise_002() -> None:
    my_string: str = "18"
    my_multiplier: int = 2
    my_number: int = int(my_string)

    if (type(my_number) == int):
        print(f"{my_number} * {my_multiplier} -> {my_number * my_multiplier}")


def exercise_003() -> None:
    msg: str = "this is some text"
    my_number: int = 17
    text: str = "Msg: " + msg.capitalize() + "." + "\nThis is a number: " + \
        str(my_number) + "."

    print(text)


def exercise_004() -> None:
    first_number: float
    second_number: float

    user_input: str = input("Type the fist number: ")

    try:
        first_number = float(user_input)
    except Exception as e:
        print(e)
        return

    user_input = input("Type the second number: ")

    try:
        second_number = float(user_input)
    except Exception as e:
        print(e)
        return

    print(f"{first_number} * {second_number} -> {first_number * second_number}")


def main() -> None:
    exercise_001()
    print()

    exercise_002()
    print()

    exercise_003()
    print()

    exercise_004()
    print()


if (__name__ == "__main__"):
    main()
