from models.calculator import Calculator


def main():
    print(Calculator.sum(10, 20, 30))
    print(Calculator.sub(100, 20, 30))


if (__name__ == "__main__"):
    main()
