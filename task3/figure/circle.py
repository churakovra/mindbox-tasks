from math import pi

from .shape import Shape

class Circle(Shape):
    def __init__(self, radius: float | int):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2
