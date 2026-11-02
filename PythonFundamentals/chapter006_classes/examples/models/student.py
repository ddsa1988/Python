from datetime import date

from .person import Person


class Student(Person):
    def __init__(self, name: str, birthdate: date, id: int) -> None:
        super().__init__(name, birthdate)
        self.id = id

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        if (type(id) != int):
            raise TypeError("id must be an integer.")

        if (id <= 0):
            raise ValueError("id must be greater tha zero.")

        self._id = id

    def get_info(self) -> str:
        return f"Name = {self.name}, Birthdate = {self.birthdate}, Age = {self.get_age()}, ID = {self.id}"

    def __str__(self) -> str:
        return f"Student (name = {self.name}, birthdate = {self.birthdate}, age = {self.get_age()}, id = {self.id})"
