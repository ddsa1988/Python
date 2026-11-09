import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path: str = f"{Path(__file__).parent}{os.sep}files"
    source_file_path: str = directory_path + os.sep + "mad_libs_source_1.txt"
    target_file_path: str = directory_path + os.sep + "mad_libs_target_1.txt"

    if (not os.path.isfile(source_file_path)):
        logger.warning(f"Source file not found: {source_file_path}")
        return

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

    source_text: str = ""

    try:
        with open(file=source_file_path, mode="r", encoding="utf-8") as file:
            source_text = file.read().strip()
    except PermissionError as ex:
        logger.warning(f"Insufficient permissions to read file: {ex}")
        return
    except OSError as ex:
        logger.warning(f"Failed to read file: {ex}")
        return

    print(source_text)

    adjective: str = ""
    noun_1: str = ""
    noun_2: str = ""
    verb: str = ""

    while (True):
        adjective = input("Enter an adjective: ")

        if (len(adjective.strip()) == 0):
            print("Invalid adjective.")
            continue

        break

    while (True):
        noun_1 = input("Enter a noun: ")

        if (len(noun_1.strip()) == 0):
            print("Invalid noun.")
            continue

        break

    while (True):
        verb = input("Enter a verb: ")

        if (len(verb.strip()) == 0):
            print("Invalid verb.")
            continue

        break

    while (True):
        noun_2 = input("Enter a noun: ")

        if (len(noun_2.strip()) == 0):
            print("Invalid noun.")
            continue

        break

    new_text: str = source_text.replace("ADJECTIVE", adjective.strip().lower())
    new_text = new_text.replace("NOUN", noun_1.strip().lower(), 1)
    new_text = new_text.replace("NOUN", noun_2.strip().lower())
    new_text = new_text.replace("VERB", verb.strip().lower())

    try:
        with open(file=target_file_path, mode="w", encoding="utf-8") as file:
            file.write(new_text)
    except PermissionError as ex:
        logger.warning(f"Insufficient permissions to write file: {ex}")
    except OSError as ex:
        logger.warning(f"Failed to write file: {ex}")


if (__name__ == "__main__"):
    main()
