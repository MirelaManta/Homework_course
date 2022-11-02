from implem2 import compare
from math import sqrt

def test_positive():
    assert compare(8, 2) == 1
    assert compare(10, 10) == 0
    assert compare(4, 9) == -1


def test_negatives():
    assert compare(-9, -6) == -1
    assert compare(-2, -7) == 1
    assert compare(-3, -3) == 0


def test_complex():
    assert compare(pow(2, 4), sqrt(256)) == 0
    assert compare(sqrt(60), 7.5) == 1
