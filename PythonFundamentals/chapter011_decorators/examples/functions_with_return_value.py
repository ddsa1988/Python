import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")  # Arbitrary number of parameters
T = TypeVar("T")  # Generic type

# Callable[P, T] => Keep the function generic signature.


def do_twice(func: Callable[P, T]) -> Callable[P, T]:

    @functools.wraps(func)
    def wrapper_do_twice(*args: P.args, **kwargs: P.kwargs) -> T:
        func(*args, **kwargs)

        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def get_greeting(name: str) -> str:
    print("Creating greeting...")

    return "Hello, " + name.strip().title() + "."


def main() -> None:
    print(get_greeting("diego"))


if (__name__ == "__main__"):
    main()
