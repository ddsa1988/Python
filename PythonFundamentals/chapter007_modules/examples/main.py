from calculator import add
from modules.calculator import sub


def main() -> None:

    print("Result = ", add(10, 20, 30))
    print("Result = ", sub(100, 20, 30))


if (__name__ == "__main__"):
    main()
