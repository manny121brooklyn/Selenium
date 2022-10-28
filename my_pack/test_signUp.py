import pytest

@pytest.fixture()
def setUpMethod():
    print('Opening URL to signup')
    yield
    print('Closing browser after signup')

def test_signUPByEmail():
    print('This is signup email test')

def test_SignUpByFacebook():
    print('This is signup by facebook test')