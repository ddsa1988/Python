import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    folder_path: str = f"{Path(__file__).parent}{os.sep}new_folder{os.sep}test"

    path: Path = Path(folder_path)

    if (path.exists()):
        logger.debug(f"Folder already exists: {folder_path}")
        return

    os.makedirs(folder_path)

    # Path("path").mkdir() can only make one directory at a time; it won’t make several subdirectories at once,
    # like os.makedirs() will.

    # path.mkdir()


if (__name__ == "__main__"):
    main()
