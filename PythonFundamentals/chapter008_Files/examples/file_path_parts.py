import logging
import os
from pathlib import Path


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    folder_path: str = f"{Path(__file__).parent}{os.sep}new_folder{os.sep}test"
    path: Path = Path(folder_path)

    logger.warning("Starting...")

    print(path.parent)
    print(path.parents[0])
    print(path.parents[1])
    print(path.parents[2])
    print(path.name)
    print(path.name)
    print(path.stem)
    print(path.suffix)
    print(path.drive)


if (__name__ == "__main__"):
    main()
