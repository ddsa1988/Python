guest_list: list[str] = ["Diego", "Amanda", "Amora", "Ameixa"]
print(guest_list)
print()

guest_who_cant_come: str = "Amora"
new_guest: str = "Ivanice"

if guest_who_cant_come in guest_list:
    index = guest_list.index(guest_who_cant_come)
    del guest_list[index]
    guest_list.insert(index, new_guest)

print(guest_list)
