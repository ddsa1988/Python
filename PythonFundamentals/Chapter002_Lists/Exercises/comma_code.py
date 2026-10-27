def list_to_string(arr: list[str]) -> str:
    if (type(arr) != list):
        TypeError("Arr must be a list type.")

    if (len(arr) == 0):
        return ""

    new_string: str = ""

    for i in range(len(arr) - 1):
        new_string += f"{arr[i]}, "

    new_string += f"and {arr[-1]}"

    return new_string


def main():
    spam: list[str] = ["apples", "bananas", "tofu", "cats"]

    print(list_to_string(spam))
    print(list_to_string([]))


if (__name__ == "__main__"):
    main()
