my_pizzas = ["pepperoni", "margarita", "portuguese"]
your_pizzas = my_pizzas.copy()

my_pizzas.append("chocolate")
your_pizzas.append("broccoli")

for pizza in my_pizzas:
    print(pizza, end=" ")

print("\n")

for pizza in your_pizzas:
    print(pizza, end=" ")
