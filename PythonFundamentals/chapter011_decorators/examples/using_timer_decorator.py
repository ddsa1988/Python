from decorators import timer


def wast_some_time(number_times: int) -> None:
    if (type(number_times) != int):
        raise TypeError("number_times must be an integer type.")

    for _ in range(number_times):
        sum([number ** 2 for number in range(10_000)])


@timer
def main() -> None:
    wast_some_time(number_times=10_000)


if (__name__ == "__main__"):
    main()
