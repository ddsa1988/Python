import logging
import os
from pathlib import Path

# '*' -> matches any text
# '?' -> matches exactly one character


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    file_path: str = f"{Path(__file__).parent}{os.sep}files"

    path: Path = Path(file_path)

    logger.debug("Starting...")

    if (not path.is_dir()):
        logger.debug(f"Directory do not exist: {file_path}")

    for name in path.glob("*.txt"):
        print(name)


if (__name__ == "__main__"):
    main()
