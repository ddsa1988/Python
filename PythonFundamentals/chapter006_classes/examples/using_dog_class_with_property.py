from models.dog_class_with_property import Dog


def main() -> None:
    dog_1: Dog = Dog(name="amora", age=2)

    print(dog_1)
    print(dog_1.__repr__())
    print()

    print(dir(dog_1))


if (__name__ == "__main__"):
    main()
