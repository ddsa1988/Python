from datetime import date, timedelta


class Person:
    def __init__(self, name: str, birthdate: date) -> None:
        self.name = name
        self.birthdate = birthdate

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if (type(name) != str):
            raise TypeError("name must be a string type.")

        if (len(name.strip()) == 0):
            raise ValueError("name can't be empty.")

        self._name = name.title()

    @property
    def birthdate(self) -> date:
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate: date) -> None:
        if (type(birthdate) != date):
            raise TypeError("birthdate must be a date type.")

        today: date = date.today()
        diff: timedelta = today - birthdate

        if (diff.days < 0):
            raise ValueError("birthdate must be greater or equal than today.")

        self._birthdate = birthdate

    def get_age(self) -> int:
        today: date = date.today()
        diff: timedelta = today - self.birthdate
        age: int = (diff / 365).days

        return age

    def get_info(self) -> str:
        return f"Name = {self.name}, Birthdate = {self.birthdate}, Age = {self.get_age()}"

    def __str__(self) -> str:
        return f"Person (name = {self.name}, birthdate = {self.birthdate}, age = {self.get_age()})"
