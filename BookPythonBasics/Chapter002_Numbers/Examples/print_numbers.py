def main() -> None:
    number: float = 7.1256
    big_number: float = 100000000.0
    ratio: float = 0.9

    print(f"{number:.1f}")
    print(f"{number:.2f}")

    print(f"{big_number:,}")
    print(f"{big_number:,.2f}")

    print(f"{ratio:.1%}")
    print(f"{ratio:.2%}")


if (__name__ == "__main__"):
    main()
