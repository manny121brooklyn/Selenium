import pytest

@pytest.fixture()
def setUpMethod():
    print('Opening URL to login')
    yield
    print('Closing browser after login')

def test_loginByEmail():
    print('This is login email test')

def test_loginByFacebook():
    print('This is login by facebook test')