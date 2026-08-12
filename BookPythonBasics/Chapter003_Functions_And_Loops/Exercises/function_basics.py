def cube(number: float) -> float:
    result: float = number ** 3

    return result


def greet(name: str) -> None:
    print(f"Hello {name}!")


def exercise_001() -> None:
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
