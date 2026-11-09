def main() -> None:
    numbers: list[int] = list(range(1, 1_000_001))

    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))


if (__name__ == "__main__"):
    main()
