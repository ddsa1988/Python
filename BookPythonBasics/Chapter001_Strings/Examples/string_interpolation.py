from datetime import date


def main() -> None:
    my_name: str = "diego"
    my_birthdate: date = date(1988, 1, 22)

    print("My name is", my_name, " and I was born in", str(my_birthdate), ".")

    print("My name is " + my_name +
          " and I was born in " + str(my_birthdate) + ".")

    print("My name is {} and I was born in {}.".format(my_name, my_birthdate))

    print("My name is {name} and I was born in {birthdate}.".format(
        name=my_name, birthdate=my_birthdate))

    print(f"My name is {my_name} and I was born in {my_birthdate}.")


if (__name__ == "__main__"):
    main()
