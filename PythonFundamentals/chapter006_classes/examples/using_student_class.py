from datetime import date

from models.person import Person


def main():
    p1: Person = Person("diego", date(1988, 1, 22))

    print(p1)
    print(p1.get_info())


if (__name__ == "__main__"):
    main()
