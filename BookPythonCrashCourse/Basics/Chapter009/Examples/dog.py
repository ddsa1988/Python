class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name: str, age: int):
        """Initialize name and sge attributes"""
        self.name: str = name
        self.age: int = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate  a dog rolling over in response to a command"""
        print(f"{self.name} rolled over")

    def __eq__(self, other: Dog):
        """Compare if two dog objects are equals"""
        if not isinstance(other, Dog):
            return NotImplemented

        return self.name == other.name and self.age == other.age

    def __str__(self):
        """Object user-friendly representation"""
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        """Object unambiguous representation that mimics the constructor"""
        return f"Dog(name = {self.name}, age = {self.age})"
