def greet(name: str) -> None:
    print(f"Hello {name}!")


def exercise_001() -> None:

    def cube(number: float) -> float:
        return number ** 3

    print(f"{cube(3):.0f}")
    print(f"{cube(9):.0f}")


def exercise_002() -> None:
    greet("Diego")


def main() -> None:
    exercise_001()
    print()

    exercise_002()
    print()


if (__name__ == "__main__"):
    main()
