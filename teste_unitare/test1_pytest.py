from implem1 import max_value
from math import sqrt


def test_simplu():
    assert max_value(12, 28, -9) == 28
    assert max_value(5, 9, 17) == 17


def test_complex():
    assert max_value(sqrt(625), 12, pow(5, 3)) == pow(5, 3)
    assert max_value(-9, - sqrt(144), - pow(2, 3)) == - pow(2, 3)
    assert max_value(sqrt(60), 8.5, 10.5) == 10.5


def test_positives():
    assert max_value(12, 5, 29) == 29
    assert max_value(2, 15, 9) == 15


