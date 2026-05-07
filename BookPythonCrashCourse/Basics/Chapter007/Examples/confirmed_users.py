unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while (len(unconfirmed_users) > 0):
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)

    print(f"Verifying user: {current_user.title()}")

print("\nThe following users have been confirmed:")

for user in confirmed_users:
    print(user.title())
