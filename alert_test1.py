import HtmlTestRunner
# import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import pytest

# from selenium.webdriver.common.alert import Alert

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
# URL = "https://testautomationpractice.blogspot.com/"
# driver.get(URL)
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//*[@onclick='myFunction()']").click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
#
# driver.quit()

# headless mode

# chrome_options = Options()
# chrome_options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#
# print(driver.title)
# print(driver.current_url)
# URL = "https://testautomationpractice.blogspot.com/"
# driver.get(URL)
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//*[@onclick='myFunction()']").click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
#
# driver.quit()

# class TestAlertButton(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         print(self.driver.title)
#         print(self.driver.current_url)
#         URL = "https://testautomationpractice.blogspot.com/"
#         self.driver.get(URL)
#         time.sleep(2)
#
#     def test_alert_box(self):
#         driver = self.driver
#         driver.find_element(By.XPATH, "//*[@onclick='myFunction()']").click()
#         alert = driver.switch_to.alert
#         time.sleep(2)
#         print(alert.text)
#         alert.accept()
#         time.sleep(2)
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))


    # pytest


class TestAlertButton:
    @pytest.fixture(scope="module")
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        URL = "https://testautomationpractice.blogspot.com/"
        self.driver.get(URL)

        yield
        self.driver.quit()

    def test_alertbox(self, setup_method):
        driver = self.driver
        self.driver.find_element(By.XPATH, "//*[@onclick='myFunction()']").click()
        alert = self.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
