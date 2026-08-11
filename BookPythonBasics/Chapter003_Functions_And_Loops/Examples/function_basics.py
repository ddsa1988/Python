def multiply(x: int, y: int) -> int:    # Function signature
    """Return the product of two numbers x and y"""

    # Function body
    product: int = x * y

    return product


def main() -> None:
    func_reference = multiply

    print(multiply(10, 2))

    print(func_reference(20, 3))


if (__name__ == "__main__"):
    main()
