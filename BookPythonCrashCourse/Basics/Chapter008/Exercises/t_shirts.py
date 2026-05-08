def make_shirt(size: str, message: str) -> None:
    print(
        f"You'd like a {size} t-shirt with the message '{message.capitalize()}'.")


make_shirt("small", "i love traveling")

print()

make_shirt(message="I like pizza", size="large")
