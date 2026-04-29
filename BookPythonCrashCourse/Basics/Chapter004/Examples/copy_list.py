original_list = ['Diego', "Amanda", "Eduarda"]
same_list = original_list
copied_list = original_list[:]

original_list.append("Amora")
same_list.append("Ameixa")
copied_list.append("Nina")

print(f"Original list: {", ".join(original_list)}")
print(f"Same list: {", ".join(same_list)}")
print(f"Copied list: {", ".join(copied_list)}")
