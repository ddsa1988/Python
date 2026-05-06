users = {
    "diego": {
        "first_name": "diego",
        "last_name": "alexander",
        "location": "curitiba"
    },

    "amanda": {
        "first_name": "amanda",
        "last_name": "perna",
        "location": "curitiba"
    }
}

print(f"{users}\n")

for user, user_info in users.items():
    print(f"user: {user} => user info:", end=" ")

    for key, value in user_info.items():
        print(f"{key}: {value}", end=", ")

    print("\n")
