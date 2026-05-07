sandwich_orders = ["grilled cheese", "club",
                   "chicken", "ham", "avocado toast", "salmon bagel"]

finished_sandwiches = []

while (len(sandwich_orders) > 0):
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich.lower())

    print(f"I made your {sandwich} sandwich.")

print("\n***** Sandwiches made *****")

for sandwich in finished_sandwiches:
    print(sandwich.capitalize())
