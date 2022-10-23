import unittest

class SignupTest(unittest.TestCase):

    def test_signup_by_email(self):
        print("This is signup test by email")
        self.assertTrue(True)

    def test_signup_by_facebook(self):
        print("This is signup test by facebook")
        self.assertTrue(True)

    def test_signup_by_twitter(self):
        print("This is signup test by twitter")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()