class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name: str, age: int) -> None:
        """Initialize name and age attributes"""
        self.set_name(name=name)
        self.set_age(age=age)

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name.title()

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        self._age = age

    def sit(self) -> None:
        print(f"{self._name} is now sitting.")

    def roll_over(self) -> None:
        print(f"{self._name} rolled over!")

    def __str__(self) -> str:
        return f"Name = {self.get_name()}, Age = {self.get_age()}"

    def __repr__(self) -> str:
        return f"Dog (Name = {self.get_name()}, Age = {self.get_age()})"

    def __eq__(self, other: object) -> bool:
        if (not isinstance(other, Dog)):
            return False

        return self.get_name() == other.get_name() and self.get_age() == other.get_age()

    def __hash__(self) -> int:
        return hash((self.get_name(), self.get_age()))
