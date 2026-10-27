import datetime as dt


def main():
    birthdays: dict[str, dt.datetime]

    while (True):
        user_name: str = input("Enter a name: (black to quit): ")

        if (len(user_name.strip()) == 0):
            break

    # print(dt.datetime.now())
    # print(dt.datetime(1988, 1, 22))
    # print((dt.datetime.now() - dt.datetime(1988, 1, 22)).days/365)


if (__name__ == "__main__"):
    main()
