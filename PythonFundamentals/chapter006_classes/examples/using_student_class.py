from datetime import date

from models.person import Person
from models.student import Student


def main() -> None:
    person: Person = Person("diego", date(1988, 1, 22))
    student: Student = Student("Amanda", date(1993, 10, 16), id=10)

    print(person)
    print(person.get_info())
    print()

    print(student)
    print(student.get_info())
    print()

    people: list[Person] = [person, student]

    for p in people:
        print(p)
        print(p.get_info())
        print()

        # try:
        #     print(p.id)
        # except AttributeError as ex:
        #     print(ex)

        # print()


if (__name__ == "__main__"):
    main()
