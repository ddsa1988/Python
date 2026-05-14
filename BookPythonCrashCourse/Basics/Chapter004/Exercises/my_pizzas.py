my_pizzas: list[str] = ["pepperoni", "margarita", "portuguese"]
your_pizzas: list[str] = my_pizzas.copy()

my_pizzas.append("chocolate")
your_pizzas.append("broccoli")

for pizza in my_pizzas:
    print(pizza, end=" ")

print("\n")

for pizza in your_pizzas:
    print(pizza, end=" ")
