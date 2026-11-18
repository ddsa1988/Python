from datetime import date
from decimal import Decimal

from .person import Person


class Employee(Person):
    def __init__(self, name: str, birthdate: date, annual_salary: Decimal = Decimal(0)) -> None:
        super().__init__(name, birthdate)
        self.annual_salary = annual_salary

    @property
    def annual_salary(self) -> Decimal:
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, amount: Decimal) -> None:
        if (type(amount) != Decimal):
            raise TypeError("amount must be a decimal type.")

        if (amount < 0):
            raise ValueError("amount must be greater than zero.")

        self._annual_salary = amount

    def give_raise(self, amount: Decimal = Decimal(5_000)) -> None:
        if (type(amount) != Decimal):
            raise TypeError("amount must be a decimal type.")

        if (amount < 0):
            raise ValueError("amount must be greater than zero.")

        self.annual_salary += amount

    def __str__(self) -> str:
        return f"Employee (name = {self.name}, birthdate = {self.birthdate}, age = {self.get_age()}, annual_salary = {self.annual_salary})"
