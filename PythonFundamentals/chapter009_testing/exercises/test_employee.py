import unittest
from datetime import date

from models.employee import Employee


class EmployeeTesting(unittest.TestCase):
    def test_create_employee(self) -> None:
        employee: Employee = Employee("diego", date(1988, 1, 22))

        self.assertEqual(
            str(employee), "Employee (name = Diego, birthdate = 1988-01-22, age = 38, annual_salary = 150000,)")


if (__name__ == "__main__"):
    unittest.main()
