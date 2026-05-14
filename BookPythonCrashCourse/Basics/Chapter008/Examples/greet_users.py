def greet_users(names: list[str]) -> None:
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


user_names: list[str] = ["hannah", "ty", "margot"]

greet_users(user_names)
