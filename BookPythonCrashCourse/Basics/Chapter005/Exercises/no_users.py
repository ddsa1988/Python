some_user_names = ["diego", "amanda", "admin", "eduarda"]
another_user_names = []


def greet_users(user_names):
    if (type(user_names) != list):
        return

    if (len(user_names) == 0):
        print("We need do find some users!")
        return

    for name in user_names:
        if (name.lower() == "admin"):
            print(f"Hello {name}, would you like to see a status report?")
            continue

        print(f"Hello {name}, thank you for logging again.")


greet_users(some_user_names)

print()

greet_users(another_user_names)
