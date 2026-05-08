def get_formatted_name(first_name: str, last_name: str, middle_name: str = "") -> str:

    full_name = ""

    if (len(middle_name.strip()) > 0):
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


print(get_formatted_name("diego", "alexandre"))
print(get_formatted_name("diego", "alexandre", "dos santos"))
