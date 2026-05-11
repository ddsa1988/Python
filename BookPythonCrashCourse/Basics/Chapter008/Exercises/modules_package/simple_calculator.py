def add(a: int, b: int) -> int:
    """Add two integer numbers"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two integer numbers"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two integer numbers"""
    return a * b


def divide(a: int, b: int) -> int:
    """Divide two integer numbers"""
    if (b == 0):
        return 0

    return a / b
