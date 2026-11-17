import unittest
from datetime import date

from models.employee import Employee


class EmployeeTesting(unittest.TestCase):
    def setUp(self) -> None:
        self._employee: Employee = Employee(name="diego", birthdate=date(1988, 1, 22), annual_salary=100_000)

    def tearDown(self) -> None:
        del self._employee

    def test_create_employee(self) -> None:
        # employee: Employee = Employee(name="diego", birthdate=date(1988, 1, 22), annual_salary=100_000)

        self.assertEqual(
            str(self._employee), "Employee (name = Diego, birthdate = 1988-01-22, age = 38, annual_salary = 100000)")

    def test_give_default_raise(self) -> None:
        # employee: Employee = Employee(name="diego", birthdate=date(1988, 1, 22), annual_salary=100_000)

        self._employee.give_raise()

        self.assertEqual(self._employee.annual_salary, 105_000)

    def test_give_custom_raise(self) -> None:
        # employee: Employee = Employee(name="diego", birthdate=date(1988, 1, 22), annual_salary=100_000)

        self._employee.give_raise(1_000)

        self.assertEqual(self._employee.annual_salary, 101_000)


if (__name__ == "__main__"):
    unittest.main()
