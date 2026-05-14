def make_car(brand: str, model: str, **car_dict: dict[str, str]) -> dict[str, str]:
    if (len(brand.strip()) == 0 or len(model.strip()) == 0):
        return car_dict

    car_dict["brand"] = brand.strip().title()
    car_dict["model"] = model.strip().title()

    return car_dict


car: dict[str, str] = make_car(
    "subaru", "outback", color="blue", tow_package="true")

print(car)
