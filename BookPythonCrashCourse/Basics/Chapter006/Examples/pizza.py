pizza: dict[str, any] = {
    "crust": "thin",
    "toppings": ["mushrooms", "cheese"]
}

print(f"{pizza}\n")

for topping in pizza["toppings"]:
    print(topping, end=" ")
