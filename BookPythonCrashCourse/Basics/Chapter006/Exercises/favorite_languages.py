people = ["diego", "amanda", "edward", "lisa"]

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phi": "python",
    "diego": "csharp"
}

for person in people:

    is_person_found = False

    for name in favorite_languages.keys():
        if (person.lower() == name.lower()):
            is_person_found = True
            break

    if (is_person_found):
        print(f"{person.title()}, thanks for taking the poll.")
    else:
        print(f"{person.title()}, would you like to take the poll?")
