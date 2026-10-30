# The @property decorator allows you to define getter, setter, and deleter methods for attributes

class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if (type(name) != str):
            raise TypeError("name must be a string type.")

        if (len(name.strip()) == 0):
            raise ValueError("name is empty.")

        self._name = name.title()

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if (type(age) != int):
            raise TypeError("age must be an integer.")

        if (age < 0):
            raise ValueError("age must be greater than zero.")

        self._age = age

    def sit(self) -> None:
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        print(f"{self.name} rolled over!")

    def __str__(self) -> str:
        return f"Name = {self.name}, Age = {self.age}"

    def __repr__(self) -> str:
        return f"Dog (Name = {self.name}, Age = {self.age})"
