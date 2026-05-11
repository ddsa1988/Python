def add_numbers(*numbers: int) -> int:
    result = 0

    for number in numbers:
        result += number

    return result


print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40, 50))
print(add_numbers(10))
