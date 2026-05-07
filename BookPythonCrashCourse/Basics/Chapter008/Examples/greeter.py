def greet_user(user_name: str) -> None:
    print(f"Hello, {user_name.title()}.")


def main():
    greet_user("diego")


if (__name__ == "__main__"):
    main()
