import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path: str = f"{Path(__file__).parent}{os.sep}files"

    if (not os.path.isdir(directory_path)):
        logger.warning(f"Directory not found: {directory_path}")
        return

    file_paths: list[Path] = [file for file in Path(directory_path).glob("*.txt")]

    print("Files found:\n")

    for file_path in file_paths:
        try:
            with open(file=file_path, mode="r", encoding="utf-8") as file:
                print(file.read())
        except PermissionError as ex:
            logger.warning(f"Insufficient permissions to read file: {ex}")
            return
        except OSError as ex:
            logger.warning(f"Failed to read file: {ex}")
            return


if (__name__ == "__main__"):
    main()
