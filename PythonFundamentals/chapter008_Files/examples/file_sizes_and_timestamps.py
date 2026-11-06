import logging
import os
import time
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    logger.debug("Starting...")

    file_path: str = f"{Path(__file__).parent}{os.sep}files{os.sep}pi_digits.txt"

    path: Path = Path(file_path)

    if (not path.exists()):
        logger.warning(f"File do not exist: {file_path}")
        return

    file_stats = path.stat()

    print(file_stats.st_size)
    print(file_stats.st_mtime)

    print(time.asctime(time.localtime(file_stats.st_mtime)))
    print(time.asctime(time.localtime(file_stats.st_ctime)))
    print(time.asctime(time.localtime(file_stats.st_atime)))


if (__name__ == "__main__"):
    main()
