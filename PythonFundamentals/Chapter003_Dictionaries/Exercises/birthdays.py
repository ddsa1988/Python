from datetime import date, datetime


def main() -> None:
    birthdays: dict[str, date] = {}
    date_object: date | None = None

    while (True):
        name: str = input("Enter a name: (black to quit): ")

        if (len(name.strip()) == 0):
            break

        name = name.title()

        if (name in birthdays):
            print(f"{birthdays.get(name, datetime.now())} is the birthday of {name}")
        else:
            while (True):
                date_string: str = input("Birthday (yyyy/mm/dd): ")

                date_object = datetime.strptime(
                    date_string, "%Y/%m/%d").date()

                try:
                    date_object = datetime.strptime(
                        date_string, "%Y/%m/%d").date()

                    birthdays[name] = date_object

                    print("Database updated.")

                    break
                except ValueError as ex:
                    print(f"Invalid date = {ex}")


if (__name__ == "__main__"):
    main()
