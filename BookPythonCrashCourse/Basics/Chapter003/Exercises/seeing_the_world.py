places_to_visit: list[str] = ["Spain", "Portugal", "China", "Italy", "Africa", "Norway",
                              "Iceland", "Atacama"]

print(f"Original list: [{", ".join(places_to_visit)}]")
print()

print(sorted(places_to_visit))
print()

print(sorted(places_to_visit, reverse=True))
print()

places_to_visit.sort()
print(places_to_visit)
print()

places_to_visit.sort(reverse=True)
print(places_to_visit)
