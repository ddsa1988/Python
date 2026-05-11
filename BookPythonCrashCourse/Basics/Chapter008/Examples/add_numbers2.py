def add_numbers(start_value: int = 0, *numbers: int) -> int:
    result = start_value

    for number in numbers:
        result += number

    return result


print(add_numbers(100, 10, 20, 30))
print(add_numbers(1000, 10, 20, 30, 40, 50))
print(add_numbers(90, 10))
