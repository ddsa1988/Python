import os
from pathlib import Path


def main() -> None:
    print(Path.cwd())
    print(Path.home())

    print(os.sep)


if (__name__ == "__main__"):
    main()
