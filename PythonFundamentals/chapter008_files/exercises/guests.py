import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path: str = f"{Path(__file__).parent}{os.sep}files"
    file_path: str = f"{directory_path}{os.sep}guest.txt"

    while (True):
        user_input: str = input("Write you name: ")

        if (len(user_input.strip()) == 0):
            break

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

        try:
            with open(file=file_path, mode="a", encoding="utf-8") as file:
                file.write(user_input.strip().title() + "\n")
        except PermissionError as ex:
            logger.warning(f"Insufficient permissions to write file: {ex}")
        except OSError as ex:
            logger.warning(f"Failed to write file: {ex}")


if (__name__ == "__main__"):
    main()
