def fahrenheit_to_celsius(temperature: float) -> float:
    result: float = (temperature - 32) * 5 / 9

    return result


def celsius_to_fahrenheit(temperature: float) -> float:
    result: float = temperature * (9 / 5) + 32

    return result


def main() -> None:
    temperature: float

    prompt: str = "Enter a temperature in degrees F: "
    user_input: str = input(prompt)

    try:
        temperature = float(user_input)
        temperature = int(
            temperature) if temperature.is_integer() else temperature
    except:
        print("Invalid temperature.")
        return

    result: float = fahrenheit_to_celsius(temperature)

    print(f"{temperature} degrees in F = {result:.2f} degrees in C.\n")

    prompt = "Enter a temperature in degrees C: "
    user_input = input(prompt)

    try:
        temperature = float(user_input)
        temperature = int(
            temperature) if temperature.is_integer() else temperature
    except:
        print("Invalid temperature.")
        return

    result: float = celsius_to_fahrenheit(temperature)

    print(f"{temperature} degrees in C = {result:.2f} degrees in F.\n")


if (__name__ == "__main__"):
    main()
