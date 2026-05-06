favorite_places = {
    "diego": ["Portugal", "Australia", "Brazil"],
    "amanda": ["France", "Italy", "Germany", "India"],
    "eduarda": ["China", "England"]
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are: ", end=" ")

    for i in range(len(places)-1):
        print(places[i].title(), end=", ")

    print(f"{places[-1].title()}.\n")
