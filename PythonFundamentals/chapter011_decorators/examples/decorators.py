import functools
import time
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def timer(func: Callable[P, T]) -> Callable[P, T]:
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args: P.args, **kwargs: P.kwargs) -> T:
        start_time: float = time.perf_counter()

        value: T = func(*args, **kwargs)

        end_time: float = time.perf_counter()

        run_time: float = end_time - start_time

        print(f"Finished {func.__name__}() in {run_time:.4f} seconds.")

        return value

    return wrapper_timer
