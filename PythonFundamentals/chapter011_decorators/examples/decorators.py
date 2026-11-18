from collections.abc import Callable
from typing import ParamSpec, TypeVar


P = ParamSpec("P")  # Arbitrary number of parameters
T = TypeVar("T")  # Generic type

# Callable[P, T] => Keep the function generic signature.


def do_twice(func: Callable[P, T]) -> Callable[P, None]:
    def wrapper_do_twice(*args: P.args, **kwargs: P.kwargs) -> None:
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice
