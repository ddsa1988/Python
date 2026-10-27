def main() -> None:
    base: float
    exponent: float
    user_input: str

    while (True):
        user_input = input("Enter a base: ")

        try:
            base = float(user_input)
            break

        except ValueError:
            print("Invalid base number.")

    while (True):
        user_input = input("Enter an exponent: ")

        try:
            exponent = float(user_input)
            break

        except ValueError:
            print("Invalid exponent number.")

    print(f"{base} to the power of {exponent} = {pow(base=base, exp=exponent):.3f}")


if (__name__ == "__main__"):
    main()
