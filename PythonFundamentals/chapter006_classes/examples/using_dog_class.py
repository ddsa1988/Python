from PythonFundamentals.chapter006_classes.models.dog_class import Dog

# from chapter006_classes execute python3 -m examples.using_dog_class


def main() -> None:
    dog_1: Dog = Dog(name="ameixa", age=2)
    dog_2: Dog = Dog(name="amora", age=3)
    dog_3: Dog = Dog(name="ameixa", age=2)

    print(dog_1)
    print(dog_2)
    print(dog_3)
    print()

    print(dog_1.get_name())
    print(dog_1.get_age())
    print()

    dog_2.sit()
    dog_2.roll_over()
    print()

    print(dog_1.__repr__())
    print(dog_2.__repr__())
    print(dog_3.__repr__())
    print()

    print(dog_1.__eq__(dog_2))
    print(dog_1.__eq__(dog_3))
    print()

    print(dog_1.__hash__())
    print(dog_2.__hash__())
    print(dog_3.__hash__())


if (__name__ == "__main__"):
    main()
