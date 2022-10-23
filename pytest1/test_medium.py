import pytest


def func(x):
    return x + 1

def test_correct():
    assert func(4) == 5

def test_false_answer():
    with pytest.raises(AssertionError):
        assert func(3)==8

def test_zero_division():
    # with pytest.raises(ZeroDivisionError):
    assert 3/0 == 1
