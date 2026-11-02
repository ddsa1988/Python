from dataclasses import dataclass

from .shape import Shape


@dataclass
class Square(Shape):
    side: float

    def get_area(self) -> float:
        return self.side * self.side
