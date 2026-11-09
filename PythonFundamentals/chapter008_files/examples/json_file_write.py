import json
import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path: str = f"{Path(__file__).parent}{os.sep}files"
    file_path: str = directory_path + os.sep + "my_obj.json"

    if (not os.path.isdir(directory_path)):
        try:
            path: Path = Path(directory_path)
            path.mkdir()
        except PermissionError as ex:
            logger.warning(f"Insufficient permissions to create directory: {ex}")
        except OSError as ex:
            logger.warning(f"Failed to create directory: {ex}")

    my_obj: dict[str, str | list[int]] = {
        "name": "Diego Alexander",
        "birthdate": "22-01-1988",
        "numbers": [2, 3, 5, 7, 11, 13]
    }

    content: str = json.dumps(obj=my_obj, indent=4)

    try:
        with open(file=file_path, mode="w", encoding="utf-8") as file:
            file.write(content)
    except PermissionError as ex:
        logger.warning(f"Insufficient permissions to write file: {ex}")
        return
    except OSError as ex:
        logger.warning(f"Failed to write file: {ex}")
        return


if (__name__ == "__main__"):
    main()
