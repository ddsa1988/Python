import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    file_path: str = f"{Path(__file__).parent}{os.sep}files{os.sep}pi_digits.txt"

    path: Path = Path(file_path)

    if (not Path.is_file(path)):
        logger.debug(f"File path not found: {file_path}")
        return

    with open(file=path, mode="r", encoding="utf-8") as file:
        content: str = file.read().strip()

        print(content)
        print()

        lines: list[str] = content.splitlines()

        for index, value in enumerate(lines, 1):
            print(f"Line {index} - {value.strip()}")


if (__name__ == "__main__"):
    main()
