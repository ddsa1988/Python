import json
import logging
import os
from pathlib import Path

from models.user import User


def create_directory(path: str) -> bool:
    if (not os.path.isdir(path)):
        try:
            dir_path: Path = Path(path)
            dir_path.mkdir()
        except PermissionError as _:
            return False
        except OSError as _:
            return False

    return True


def user_to_dict(user: User) -> dict[str, str]:
    return {
        "name": user.name,
        "favorite_number": str(user.favorite_number)
    }


def write_file(path: str, content: str) -> bool:
    try:
        with open(file=path, mode="w", encoding="utf-8") as file:
            file.write(content)
    except (PermissionError, OSError) as _:
        return False

    return True


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    directory_path: str = str(Path(__file__).parent) + os.sep + "files"
    file_path: str = directory_path + os.sep + "favorite_number.json"

    is_dir: bool = create_directory(path=directory_path)

    if (not is_dir):
        logger.warning("Failed to create directory " + directory_path)

    users: list[User] = []

    while (True):
        user_input: str = ""
        name: str = ""
        number: int | None = None

        user_input = input("Type the user name: ").strip()

        if (user_input == ""):
            break

        name = user_input.lower()

        while (True):
            user_input = input("Type the user favorite number: ").strip()

            if (user_input == ""):
                break

            try:
                number = int(user_input)
            except TypeError as _:
                print("Invalid number.")
                continue

            break

        if (number == None):
            break

        user: User = User(name=name, favorite_number=number)
        users.append(user)

        print()

    if (len(users) == 0):
        return

    users_dict: list[dict[str, str]] = [user_to_dict(user) for user in users]

    json_content: str = json.dumps(users_dict, indent=4)

    write_file(file_path, json_content)


if (__name__ == "__main__"):
    main()
