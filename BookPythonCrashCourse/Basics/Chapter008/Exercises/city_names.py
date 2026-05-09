def city_country(city: str, country: str) -> str:
    return f"{city.capitalize()}, {country.capitalize()}"


print(city_country("curitiba", "brazil"))

print()

print(city_country("paris", "france"))

print()

print(city_country("lisbon", "portugal"))
