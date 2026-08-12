def main() -> None:
    n: int = 0

    while (n < 5):
        print(n, end=" ")

        n += 1

    n = 10

    print()

    while (n > 0):
        print(n, end=" ")

        n -= 1

        if (n == 5):
            break


if (__name__ == "__main__"):
    main()
