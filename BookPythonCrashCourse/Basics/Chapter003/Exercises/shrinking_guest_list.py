def cancel_dinner_msg(name: str) -> None:
    if (type(name) != str):
        return

    print(f"I'll have to cancel our dinner {name}. I'm sorry.")


guest_list = ["Diego", "Amanda", "Amora", "Ameixa",
              "Ivanice", "Tainara", "Rodrigo", "Mireli"]

print(guest_list)
print()

while (len(guest_list) > 2):
    popped_name = guest_list.pop()
    cancel_dinner_msg(popped_name)

print()
print(guest_list)

while (len(guest_list) > 0):
    del guest_list[0]

print()
print(guest_list)
