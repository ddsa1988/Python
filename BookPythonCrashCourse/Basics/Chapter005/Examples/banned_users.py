banned_users = ["andrew", "carolina", "david"]

user = "carolina"

if (user in banned_users):
    print(f"{user}. You're banned.")

print()

user = "maria"

if (user not in banned_users):
    print(f"{user}. You're not banned.")
