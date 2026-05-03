current_users = ["diego", "amanda", "eduarda", "amora", "ameixa"]
new_users = ["ivanice", "DIEGO", "rodrigo", "mireli", "AmAnDa"]

for user in new_users:
    if (user.lower() in current_users):
        print(
            f"{user}, this name is already in use. You will need to enter a new username")
        continue

    print(f"{user}, this name is available")
