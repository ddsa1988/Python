cities = {
    "curitiba": {
        "state": "parana",
        "country": "brazil",
        "population": 50000
    },

    "bonito": {
        "state": "mato grosso sul",
        "country": "brazil",
        "population": 20000
    },

    "recipe": {
        "state": "pernambuco",
        "country": "brazil",
        "population": 60000
    },

    "porto_alegre": {
        "state": "rio grande do sul",
        "country": "brazil",
        "population": 55000
    }
}

for city, city_info in cities.items():
    print(f"City: {city.title()}")

    for key, value in city_info.items():
        print(f"{key.title()}: {str(value).title()}")

    print()
