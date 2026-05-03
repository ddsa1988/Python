numbers = list(range(1, 10))

for number in numbers:
    if (number == 1):
        print(f"{number}st")
        continue

    if (number == 2):
        print(f"{number}nd")
        continue

    if (number == 3):
        print(f"{number}rd")
        continue

    print(f"{number}th")
