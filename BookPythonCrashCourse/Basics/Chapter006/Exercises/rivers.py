rivers = {
    "amazonas": "brazil",
    "nile": "egypt",
    "yangtze": "china",
    "mississippi": "united states"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()

for river in rivers.keys():
    print(river.title(), end=" ")

print('\n')

for country in rivers.values():
    print(country.title(), end=" ")
