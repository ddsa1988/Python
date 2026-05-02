user_names = ["diego", "amanda", "admin", "eduarda"]

for name in user_names:
    if (name.lower() == "admin"):
        print(f"Hello {name}, would you like to see a status report?")
        continue

    print(f"Hello {name}, thank you for logging again.")
