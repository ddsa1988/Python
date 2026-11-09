import json
import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    file_path: str = f"{Path(__file__).parent}{os.sep}files{os.sep}my_obj.json"

    if (not os.path.isfile(file_path)):
        logger.warning(f"File not found: {file_path}")
        return

    my_obj: dict[str, str | list[int]] = {}

    try:
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            content: str = file.read()
            my_obj = json.loads(content)
    except PermissionError as ex:
        logger.warning(f"Insufficient permissions to write file: {ex}")
        return
    except OSError as ex:
        logger.warning(f"Failed to write file: {ex}")
        return

    print(my_obj)


if (__name__ == "__main__"):
    main()
