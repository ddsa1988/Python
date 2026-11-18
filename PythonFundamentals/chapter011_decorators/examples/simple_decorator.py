import functools
from collections.abc import Callable


def decorator(func: Callable[[], None]) -> Callable[[], None]:

    @functools.wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_good_night() -> None:
    print("Good night!")


@decorator
def say_good_morning() -> None:
    print("Good morning!")


def main() -> None:
    good_night: Callable[[], None] = decorator(say_good_night)
    good_night()

    print()

    say_good_morning()


if (__name__ == "__main__"):
    main()
