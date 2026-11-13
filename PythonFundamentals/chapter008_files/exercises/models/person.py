from datetime import date, timedelta
from json import JSONEncoder
from typing import Any


class Person(JSONEncoder):
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

        self._name = name.strip().title()

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

    def to_dict(self) -> dict[str, str]:
        return {"name": self.name, "birthdate": self.birthdate.isoformat()}

    def default(self, o: Any) -> Any:
        if isinstance(o, date):
            return o.isoformat()

        return super().default(o)

    def __str__(self) -> str:
        return f"Person [name = {self.name}, birthdate = {self.birthdate}]"
