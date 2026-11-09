import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    file_path: str = f"{Path(__file__).parent}{os.sep}files{os.sep}pi_million_digits.txt"

    path: Path = Path(file_path)

    if (not path.is_file()):
        logger.debug(f"File path not found: {file_path}")
        return

    # with open(file=path, mode="r", encoding="utf-8") as file:
    #     for line in file:
    #         print(line)

    with open(file=path, mode="r", encoding="utf-8") as file:
        for index, line in enumerate(file, 1):
            print(f"Line {index}: {line.strip()}")


if (__name__ == "__main__"):
    main()
