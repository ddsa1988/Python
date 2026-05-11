def make_pizza(size: int, *toppings: str) -> None:
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")
