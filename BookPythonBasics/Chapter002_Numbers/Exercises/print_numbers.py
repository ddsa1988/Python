def exercise_001() -> None:
    result: float = 3 ** .125

    print(f"{result:.3f}")


def exercise_002() -> None:
    number: int = 150000

    print(f"{number:,.2f}")


def exercise_003() -> None:
    result: float = 2 / 10

    print(f"{result:.0%}")


def main() -> None:
    exercise_001()
    print()

    exercise_002()
    print()

    exercise_003()
    print()


if (__name__ == "__main__"):
    main()
