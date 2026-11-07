import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    file_path: str = f"{Path(__file__).parent}{os.sep}files{os.sep}some_text_1.txt"

    logger.debug("Starting...")

    with open(file=file_path, mode="a", encoding="utf-8") as file:
        file.write("This is some text.\n")


if (__name__ == "__main__"):
    main()
