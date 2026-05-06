pizza = {
    "crust": "thin",
    "toppings": ["mushrooms", "cheese"]
}

print(f"{pizza}\n")

for topping in pizza["toppings"]:
    print(topping, end=" ")
