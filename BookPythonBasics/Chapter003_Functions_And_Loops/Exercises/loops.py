def exercise_001() -> None:
    for number in range(2, 11):
        print(number, end=" ")


def exercise_002() -> None:
    number: int = 2

    while (number < 11):
        print(number, end=" ")

        number += 1


def exercise_003() -> None:

    def double(number: int) -> int:
        return number * 2

    number: int = 2

    # The _ ignore the index loop variable
    for _ in range(3):
        number = double(number)
        print(number, end=" ")


def main() -> None:
    exercise_001()
    print()

    exercise_002()
    print()

    exercise_003()
    print()


if (__name__ == "__main__"):
    main()
