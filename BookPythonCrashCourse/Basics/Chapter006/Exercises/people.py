import datetime as dt

diego = {
    "first_name": "diego",
    "last_name": "alexander",
    "birthdate": dt.date(1988, 1, 22),
    "country": "Brazil"
}

amanda = {
    "first_name": "amanda",
    "last_name": "perna",
    "birthdate": dt.date(1993, 10, 16),
    "country": "Brazil"
}

john = {
    "first_name": "john",
    "last_name": "scott",
    "birthdate": dt.date(1981, 5, 11),
    "country": "England"
}

people = [diego, amanda, john]

print(f"{people}\n")


print(dt.datetime.now().year - diego["birthdate"].year)
