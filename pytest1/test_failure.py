import math
import pytest


def test_sqrt():
    num  = 25
    assert math.sqrt(num) == 6


def test_square_failure():
    num = 7
    assert 7*7 == 40


def test_equality_failure():
    assert 10 == 11