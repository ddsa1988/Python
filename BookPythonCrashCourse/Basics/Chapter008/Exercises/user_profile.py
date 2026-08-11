def build_profile(first_name: str, last_name: str, **user_profile: str) -> dict[str, str]:
    if (len(first_name.strip()) == 0 or len(last_name.strip()) == 0):
        return user_profile

    user_profile["first_name"] = first_name.strip().title()
    user_profile["last_name"] = last_name.strip().title()

    return user_profile


my_profile: dict[str, str] = build_profile(
    "diego", "alexander", birthdate="1988-1-22", country="Brazil")

print(my_profile)
