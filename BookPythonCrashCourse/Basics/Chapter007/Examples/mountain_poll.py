# What is your name?
# Which mountain would you like to climb someday?
# "Would you like to let another person respond? (yes/ no)
# Poll Results

results = {}
is_poll_active = True

while (is_poll_active):
    user_name = input("What is your name? ")

    if (len(user_name.strip()) < 1):
        print("Invalid name.")
        continue

    user_response = input("Which mountain would you like to climb someday? ")

    if (len(user_response.strip()) < 1):
        print("Invalid response.")
        continue

    results[user_name.lower()] = user_response.lower()

    quit = input("Would you like to let another person respond? (yes/no) ")

    if (len(quit.strip()) > 0 and quit.lower() == "no"):
        break

print("\n--- Poll Results ---")

for name, response in results.items():
    print(f"{name.title()} would like to climb {response.title()}.")
