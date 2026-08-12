def nested_while_loop() -> None:
    print("Nested while loop:\n")

    row: int = 0

    while (row < 3):
        col: int = 0

        while (col < 4):
            print(f"row = {row}, col = {col}")
            col += 1

        row += 1

        print()


def nested_for_loop() -> None:
    print("Nested for loop:\n")

    for row in range(3):
        for col in range(4):
            print(f"row = {row}, col = {col}")

        print()


def main() -> None:
    nested_while_loop()
    print()

    nested_for_loop()
    print()


if (__name__ == "__main__"):
    main()
