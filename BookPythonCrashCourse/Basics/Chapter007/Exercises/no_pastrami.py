sandwich_orders: list[str] = ["grilled cheese", "pastrami", "club",
                              "chicken", "ham", "pastrami", "avocado toast", "salmon bagel", "pastrami"]

sandwich_excluded: str = "pastrami"

print(f"{sandwich_orders}\n")

while (sandwich_excluded in sandwich_orders):
    sandwich_orders.remove(sandwich_excluded)

print(sandwich_orders)
