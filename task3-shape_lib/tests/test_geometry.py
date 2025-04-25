import pytest
from task3-shape_lib.figure.circle import Circle
from task3-shape_lib.figure.Triangle import Triangle

def test_circle_area():
    c = Circle(2)
    assert round(c.area(), 2) == 12.57

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert round(t.area(), 2) == 6.0

def test_triangle_is_right_angled():
    t = Triangle(3, 4, 5)
    assert t.is_right_angled() == True