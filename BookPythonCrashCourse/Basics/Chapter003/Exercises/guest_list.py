def dinner_invite(names: list) -> None:
    if (type(names) != list):
        return None

    for name in names:
        print(
            f"Good morning, {name}. How are you? I would like to invite you for dinner tomorrow at my house.")


guest_list = ["Diego", "Amanda", "Amora", "Ameixa"]
print(guest_list)
print()

dinner_invite(guest_list)
print()
