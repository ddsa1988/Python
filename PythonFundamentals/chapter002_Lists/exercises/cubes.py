def main() -> None:
    cubes: list[int] = [value ** 3 for value in range(1, 10)]

    print(cubes)


if (__name__ == "__main__"):
    main()
