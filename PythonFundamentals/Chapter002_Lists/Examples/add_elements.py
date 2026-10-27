def main():
    numbers: list[int] = [10, 20, 30]

    numbers.append(100)
    numbers.insert(0, 300)

    print(numbers)


if (__name__ == "__main__"):
    main()
