def main() -> None:
    first_name: str = "Diego"
    last_name: str = "Alexander"
    full_name: str = first_name + " " + last_name
    text: str = f"My first name is {first_name} and my last name is {last_name}"

    print(f"The word '{first_name}' has {len(first_name)} letters.")
    print(f"The word '{last_name}' has {len(last_name)} letters.")
    print(f"The text '{text}' has {len(text)} letters.")
    print(f"My first name is {full_name[:5]}.")
    print(f"My last name is {full_name[6:]}.")


if (__name__ == "__main__"):
    main()
