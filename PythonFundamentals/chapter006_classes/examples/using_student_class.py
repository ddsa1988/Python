from datetime import date

from models.person import Person
from models.student import Student


def main() -> None:
    person: Person = Person("diego", date(1988, 1, 22))
    student: Student = Student("Amanda", date(1993, 10, 16))

    print(person)
    print(person.get_info())
    print()

    print(student)
    print(student.get_info())


if (__name__ == "__main__"):
    main()
