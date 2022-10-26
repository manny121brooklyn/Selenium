import pytest

# class TestClass:
#     @pytest.mark.regression
#     def test_multiply(self):
#         pass
#
#     def test_division(self):
#         pass
#
#     def test_add(self):
#         assert 4/4==1



@pytest.mark.regression
def test_multiply():
    num = 100
    assert num >= 100

def test_division():
    num = 100
    assert num < 200

def test_add():
    assert 4/4 == 1
