def sub(*args: float) -> float:
    result: float = 0

    for value in args:
        if (type(value) != int and type(value) != float):
            raise TypeError("arguments must be integer or float type.")

        result -= value

    return result
