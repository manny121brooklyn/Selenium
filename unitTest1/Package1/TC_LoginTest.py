import unittest
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    def test_login_by_email(self):
        print("This is login test by email")
        self.assertTrue(True)

    def test_login_by_facebook(self):
        print("This is login test by facebook")
        self.assertTrue(True)

    def test_login_by_twitter(self):
        print("This is login test by twitter")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
