import json
import logging
import os
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

    raise NotImplementedError


if (__name__ == "__main__"):
    main()
