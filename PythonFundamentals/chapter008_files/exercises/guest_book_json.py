import json
import logging
import os
from datetime import date, datetime
from pathlib import Path

from models.person import Person


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path: str = f"{Path(__file__).parent}{os.sep}files"
    file_path: str = directory_path + os.sep + "guest_book.json"

    if (not os.path.isdir(directory_path)):
        try:
            path: Path = Path(directory_path)
            path.mkdir()
        except PermissionError as ex:
            logger.warning(f"Insufficient permissions to create directory: {ex}")
            return
        except OSError as ex:
            logger.warning(f"Failed to create directory: {ex}")
            return

    guests: list[Person] = [Person(name="Diego Alexander", birthdate=date(1988, 1, 22)),
                            Person(name="Amanda Perna", birthdate=date(1993, 10, 16)),
                            Person(name="Eduarda Perna", birthdate=date(2026, 7, 21))]

    guests_dict: list[dict[str, str]] = [guest.to_dict() for guest in guests]
    json_content: str = ""

    try:
        json_content: str = json.dumps(guests_dict, indent=4)
    except TypeError as ex:
        logger.warning(f"Serialization error: {ex}")
        return
    except ValueError as ex:
        logger.warning(f"Invalid JSON value error: {ex}")
        return

    try:
        with open(file=file_path, mode="w", encoding="utf-8") as file:
            file.write(json_content)
    except PermissionError as ex:
        logger.warning(f"Insufficient permissions to write file: {ex}")
    except OSError as ex:
        logger.warning(f"Failed to write file: {ex}")

    _: str = input("Type any key to continue: ")

    if (not os.path.isfile(file_path)):
        logger.warning(f"File not found: {file_path}")
        return

    people: list[dict[str, str]] | None = None

    try:
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            file_content: str = file.read()
            people = json.loads(file_content)
    except PermissionError as ex:
        logger.warning(f"Insufficient permissions to write file: {ex}")
    except OSError as ex:
        logger.warning(f"Failed to read file: {ex}")

    if (people == None):
        return

    guests_from_file: list[Person] = []

    for obj in people:
        name: str | None = obj.get("name")
        date_str: str | None = obj.get("birthdate")

        if (name == None):
            continue

        if (len(name.strip()) == 0):
            continue

        if (date_str == None):
            continue

        birthdate: date

        try:
            birthdate = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as ex:
            logger.warning(f"Invalid date value: {ex}")
            continue
        except TypeError as ex:
            logger.warning(f"Invalid date type: {ex}")
            continue

        person: Person

        try:
            person = Person(name=name, birthdate=birthdate)
        except (ValueError, TypeError) as ex:
            logger.warning(f"Failed to create person object: {ex}")
            continue

        guests_from_file.append(person)

    for guest in guests_from_file:
        print(guest)


if (__name__ == "__main__"):
    main()
