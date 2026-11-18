import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def decorator(func: Callable[P, T]) -> Callable[P, T]:

    @functools.wraps(func)
    def wrapper_decorator(*args: P.args, **kwargs: P.kwargs):

        # Do something here

        value: T = func(*args, **kwargs)

        # Do something after

        return value

    return wrapper_decorator
