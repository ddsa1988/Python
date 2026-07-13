def main() -> None:
    animal: str = "Newt"
    weight: float = 0.2

    print(str(weight) + " kg is the weight of the " + animal + ".")
    print("{} kg is the weight of the {}.".format(weight, animal))
    print(f"{weight} kg is the weight of the {animal}.")


if (__name__ == "__main__"):
    main()
