from models.car import Car


def main() -> None:
    my_car: Car = Car("Ford", "Ford Ka", 2020)

    print(my_car.get_info_1())
    print(my_car.make)
    print()

    print(Car.class_variable)
    print(Car.get_info_2())


if (__name__ == "__main__"):
    main()
