counter = 0
max_count = 20
is_active = True

while (is_active):
    counter += 1

    if (counter % 2 == 0):
        continue

    print(counter, end=" ")

    if (counter == 15):
        break

    if (counter >= max_count):
        is_active = False
