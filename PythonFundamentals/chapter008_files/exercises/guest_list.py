import json
import logging
import os
from datetime import date
from pathlib import Path

from models.person import Person


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path: str = f"{Path(__file__).parent}{os.sep}files"

    if (not os.path.isdir(directory_path)):
        try:
            pass
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

    print(json_content)


if (__name__ == "__main__"):
    main()
