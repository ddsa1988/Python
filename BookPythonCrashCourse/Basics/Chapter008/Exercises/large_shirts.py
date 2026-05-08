def make_shirt(size: str = "large", message: str = "I love Python.") -> None:
    print(
        f"You'd like a {size} t-shirt with the message '{message.capitalize()}'.")


make_shirt()

print()

make_shirt("small")

print()

make_shirt(message="I love traveling")
