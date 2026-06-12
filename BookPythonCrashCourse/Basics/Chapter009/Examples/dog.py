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
