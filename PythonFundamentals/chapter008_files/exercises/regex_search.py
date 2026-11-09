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

    files: list[Path] = [file for file in Path(directory_path).glob("*.txt")]

    print("Files found:\n")

    for file in files:
        print(file)


if (__name__ == "__main__"):
    main()
