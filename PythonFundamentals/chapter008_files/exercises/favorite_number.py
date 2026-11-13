import logging
import os
from pathlib import Path


def create_directory(path: str) -> bool:
    if (not os.path.isdir(path)):
        try:
            dir_path: Path = Path(path)
            dir_path.mkdir()
        except PermissionError as _:
            return False
        except OSError as _:
            return False

    return True


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path: str = str(Path(__file__).parent) + os.sep + "files"
    file_path: str = directory_path + os.sep + "favorite_number.json"

    is_dir: bool = create_directory(path=directory_path)

    if (not is_dir):
        logger.warning("Failed to create directory " + directory_path)


if (__name__ == "__main__"):
    main()
