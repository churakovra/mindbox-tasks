from math import sqrt

from .shape import Shape


class Triangle(Shape):
    def __init__(self, a: float | int, b: float | int, c: float | int):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self) -> bool:
        sides = sorted((self.a, self.b, self.c))
        cat1, cat2, gip = sides
        return sqrt(cat1 ** 2 + cat2 ** 2) == gip
