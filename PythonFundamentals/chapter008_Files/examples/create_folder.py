import os
from pathlib import Path


def main() -> None:
    folder_path: str = f"{Path(__name__).parent}"
    print(folder_path)
    print(Path.cwd())


if (__name__ == "__main__"):
    main()
