from dataclasses import dataclass

# Automatically generates special methods like .__init__(), .__repr__(), and .__eq__()


@dataclass
class Dog:
    name: str
    age: int

    def sit(self) -> None:
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        print(f"{self.name} rolled over!")
