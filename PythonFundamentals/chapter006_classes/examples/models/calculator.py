class Calculator:

    @staticmethod
    def sum(*args: float) -> float:
        result: float = 0

        for arg in args:
            if (type(arg) != int and type(arg) != float):
                raise TypeError("arg must be an integer or float type.")

            result += arg

        return result

    @staticmethod
    def sub(*args: float) -> float:
        result: float = 0

        for arg in args:
            if (type(arg) != int and type(arg) != float):
                raise TypeError("arg must be an integer or float type.")

            result -= arg

        return result
