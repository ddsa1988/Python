def addition() -> None:
    num1: int = 9
    num2: int = 5

    print(f"{num1} + {num2} = {num1 + num2}")


def subtraction() -> None:
    num1: int = 9
    num2: int = 5

    print(f"{num1} - {num2} = {num1 - num2}")


def multiplication() -> None:
    num1: int = 9
    num2: int = 5

    print(f"{num1} * {num2} = {num1 * num2}")


def division() -> None:
    num1: int = 9
    num2: int = 5

    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2}")

    num2 *= -1

    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2}")


def exponent() -> None:
    num1: int = 9
    num2: int = 2
    num3: int = -2
    num4: float = 0.5

    print(f"{num1} ** {num2} = {num1 ** num2}")
    print(f"{num2} ** {num3} = {num2 ** num3}")
    print(f"{num1} ** {num4} = {num1 ** num4}")


def modulus() -> None:
    num1: int = 5
    num2: int = 3

    print(f"{num1} % {num2} = {num1 % num2}")

    num1 = -5
    num2 = 3

    print(f"{num1} % {num2} = {num1 % num2}")

    num1 = 5
    num2 = -3

    print(f"{num1} % {num2} = {num1 % num2}")

    num1 = -5
    num2 = -3

    print(f"{num1} % {num2} = {num1 % num2}")


def main() -> None:
    addition()
    subtraction()
    multiplication()
    division()
    exponent()
    modulus()


if (__name__ == "__main__"):
    main()
