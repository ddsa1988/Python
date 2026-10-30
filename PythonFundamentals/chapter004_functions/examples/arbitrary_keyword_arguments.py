def my_function(**kwargs: dict[str, str | int]) -> None:
    print(type(kwargs))
    print(kwargs)


def main() -> None:
    my_function(first_name="diego", last_name="alexander",  # type: ignore
                age=30)  # type: ignore


if (__name__ == "__main__"):
    main()
