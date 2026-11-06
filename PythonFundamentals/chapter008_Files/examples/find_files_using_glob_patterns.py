import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    file_path: str = f"{Path(__file__).parent}{os.sep}files{os.sep}pi_digits.txt"

    path: Path = Path(file_path)

    logger.debug("Starting...")

    if (not path.exists()):
        logger.debug(f"File do not exist: {file_path}")


if (__name__ == "__main__"):
    main()
