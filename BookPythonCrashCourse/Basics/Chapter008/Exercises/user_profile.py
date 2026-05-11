def build_profile(first_name: str, last_name: str, **user_profile: dict[str, str]) -> dict:

    if (len(first_name.strip()) <= 0 or len(last_name.strip()) <= 0):
        return user_profile

    user_profile["first_name"] = first_name
    user_profile["last_name"] = last_name

    return user_profile


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')

print(user_profile)
