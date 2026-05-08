def describe_city(city: str, country: str = "Nowhere"):
    print(f"{city.title()} is in {country.title()}.")


describe_city("curitiba")

print()

describe_city("paris", 'france')
