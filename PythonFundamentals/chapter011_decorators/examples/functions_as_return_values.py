from collections.abc import Callable

# Callable[[argument_types], return_type]


def parent(num: int):
    def first_child(name: str) -> str:
        return "Hi, I'm " + name + "."

    def second_child(name: str) -> str:
        return "Call me, " + name + "."

    if (num == 1):
        return first_child
    else:
        return second_child


def main() -> None:
    first: Callable[[str], str] = parent(1)
    print(first("diego"))

    second = parent(2)
    print(second("amanda"))


if (__name__ == "__main__"):
    main()
