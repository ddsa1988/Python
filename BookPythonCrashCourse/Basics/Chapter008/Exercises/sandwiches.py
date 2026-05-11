def sandwich_order_summary(*items: str) -> None:
    print("Sandwich items ordered:\n")

    for item in items:
        print(item.title())


sandwich_order_summary("bread", "cheese", "ham", "mayonnaise")

print()

sandwich_order_summary("italian bread", "mayonnaise", "meat")

print()

sandwich_order_summary("bread", "cheese", "meat")
