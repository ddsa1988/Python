odd_numbers = list(range(1, 30, 2))

print(odd_numbers)

print("\nThe first three items are:", end=" ")

for number in odd_numbers[:3]:
    print(number, end=" ")

middle_index = len(odd_numbers) // 2

print("\n\nThree items from the middle:", end=" ")

for number in odd_numbers[middle_index:middle_index+3]:
    print(number, end=" ")

print("\n\nThe last three items in the list are:", end=" ")

for number in odd_numbers[-3:]:
    print(number, end=" ")
