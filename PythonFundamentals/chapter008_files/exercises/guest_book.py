import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path = f"{Path(__file__).parent}{os.sep}files"
    file_path: str = f"{directory_path}{os.sep}guest_book.txt"

    guests_names: list[str] = []

    while (True):
        user_input: str = input("Write the guest name: ")

        if (len(user_input.strip()) == 0):
            break

        guests_names.append(user_input.strip().title() + "\n")

    if (len(guests_names) == 0):
        return

    if (not os.path.isdir(directory_path)):
        try:
            path: Path = Path(directory_path)
            path.mkdir()
        except PermissionError as ex:
            logger.debug(f"Insufficient permissions to create directory: {ex}")
            return
        except OSError as ex:
            logger.warning(f"Failed to create directory: {ex}")
            return

    try:
        with open(file=file_path, mode="w", encoding="utf-8") as file:
            file.writelines(guests_names)
    except PermissionError as ex:
        logger.warning(f"Insufficient permissions to write file: {ex}")
    except OSError as ex:
        logger.warning(f"Failed to write file: {ex}")


if (__name__ == "__main__"):
    main()
