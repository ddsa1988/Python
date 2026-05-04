from datetime import date

diego = {
    "first_name": "Diego",
    "last_name": "Alexander",
    "birthdate": date(1988, 1, 22),
    "country": "Brazil"
}

print(f"{diego}\n")

print(f"first name: {diego.get("first_name")}\n")

print(f"last name: {diego.get("last_name")}\n")

print(f"birthdate: {diego.get("birthdate")}\n")

print(f"country: {diego.get("country")}\n")
