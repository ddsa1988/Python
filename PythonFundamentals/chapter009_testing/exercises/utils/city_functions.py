def city_country(city: str, country: str, population: int | None = None) -> str:
    if (type(city) != str):
        raise TypeError("city must be a string type.")

    if (city.strip() == ""):
        raise ValueError("cyt can't be empty.")

    if (type(country) != str):
        raise TypeError("city must be a string type.")

    if (country.strip() == ""):
        raise ValueError("city can't be empty.")

    if (population != None and type(population) != int):
        raise TypeError("population must be an int type.")

    if (population != None and population <= 0):
        raise ValueError("population must be greater than zero.")

    if (population == None):
        return city.strip().title() + ", " + country.strip().title() + "."
    else:
        return city.strip().title() + ", " + country.strip().title() + " - population " + str(population) + "."
