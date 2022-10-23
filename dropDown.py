import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


# webdriver

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://the-internet.herokuapp.com/dropdown")
#
# a = driver.find_element(By.XPATH, "//*[@id='dropdown']")
# select = Select(a)
# select.select_by_index(1)
# time.sleep(2)
#
# select.select_by_visible_text("Option 2")
# time.sleep(2)
# driver.quit()

# Unittest

# class TestDropDownElement(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver.implicitly_wait(5)
#         self.driver.get("https://the-internet.herokuapp.com/dropdown")
#
#     def test_drop_and_down_menu(self):
#         driver = self.driver
#         a = driver.find_element(By.XPATH, "//*[@id='dropdown']")
#         select = Select(a)
#         select.select_by_index(1)
#         time.sleep(2)
#         select.select_by_visible_text("Option 2")
#         time.sleep(2)
#
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))
#


# headless mode

chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://the-internet.herokuapp.com/dropdown")

a = driver.find_element(By.XPATH, "//*[@id='dropdown']")
select = Select(a)
select.select_by_index(1)
time.sleep(2)

select.select_by_visible_text("Option 2")
time.sleep(2)

driver.quit()