def collatz(number: int) -> int:
    if (number % 2 == 0):
        return number // 2
    else:
        return 3 * number + 1


def main() -> None:
    value: int = 0

    while (True):
        user_input: str = input("Enter a number: ")

        try:
            value = int(user_input)
            break
        except ValueError:
            print("Invalid number.")

    while (True):
        print(value, end=" ")

        if (value <= 1):
            break

        value = collatz(value)


if (__name__ == "__main__"):
    main()
