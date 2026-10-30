from models.dog_class_with_data_class import Dog


def main() -> None:
    dog_1: Dog = Dog(name="ameixa", age=2)
    dog_2: Dog = Dog(name="amora", age=3)
    dog_3: Dog = Dog(name="ameixa", age=2)

    print(dog_1)
    print(dog_2)
    print(dog_3)
    print()

    print(dog_1.name)
    print(dog_1.age)
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


if (__name__ == "__main__"):
    main()
