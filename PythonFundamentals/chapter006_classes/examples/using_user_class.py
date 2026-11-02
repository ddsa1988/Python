from uuid import uuid4

from models.user import User


def main() -> None:
    user: User = User(id=uuid4(), name="Diego", email="diego@outlook.com")
    print(user)


if (__name__ == "__main__"):
    main()
