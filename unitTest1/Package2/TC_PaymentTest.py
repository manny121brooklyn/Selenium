import unittest

import HtmlTestRunner


class PaymentTest(unittest.TestCase):

    def test_payment_in_dollar(self):
        print("This is test of payment in dollar")
        self.assertTrue(True)

    def test_payment_in_euros(self):
        print("This is test payment in euros")
        self.assertTrue(True)





if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))
