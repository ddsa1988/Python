def main() -> None:
    base: float
    exponent: float

    user_input: str = input("Enter a base: ")

    try:
        base = float(user_input)
    except:
        print("Invalid number.")
        return

    user_input = input("Enter an exponent: ")

    try:
        exponent = float(user_input)
    except:
        print("Invalid number.")
        return

    result: float = base ** exponent

    print(f"{base} to the power of {exponent} = {result}")


if (__name__ == "__main__"):
    main()
