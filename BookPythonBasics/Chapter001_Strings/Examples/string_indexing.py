def main() -> None:
    flavor: str = "apple pie"

    print(f"First char: {flavor[0]}")
    print(f"Last char: {flavor[len(flavor)-1]}")

    print(f"First char: {flavor[len(flavor)*-1]}")
    print(f"Last char: {flavor[-1]}")


if (__name__ == "__main__"):
    main()
