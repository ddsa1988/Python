from models.square import Square


def main() -> None:
    square: Square = Square(10.5)

    print(square)
    print(dir(square))
    print(square.get_area())


if (__name__ == "__main__"):
    main()
