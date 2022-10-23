import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.maximize_window()
# URL = "https://testautomationpractice.blogspot.com/"
# driver.get(URL)
# try:
#     double_click = driver.find_element(By.XPATH, "//*[@ondblclick='myFunction1()']")
#     action = ActionChains(driver)
#     action.double_click(double_click).perform()
#     time.sleep(2)
#     x = driver.title
#     print(x)
#     assert x == "Automation Testing Practice - Atom"
# except:
#     driver.quit()


# headless mode

# chrome_options = Options()
# chrome_options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# # driver.implicitly_wait(10)
# # driver.maximize_window()
# URL = "https://testautomationpractice.blogspot.com/"
# driver.get(URL)
#
# double_click = driver.find_element(By.XPATH, "//*[@ondblclick='myFunction1()']")
# action = ActionChains(driver)
# action.double_click(double_click).perform()
# # time.sleep(2)
# x = driver.title
# print(x)
#
# driver.quit()

# unittest

# class TestDoubleClickMethod(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         URL = "https://testautomationpractice.blogspot.com/"
#         self.driver.get(URL)
#
#     def test_double_click_on_button(self):
#         driver = self.driver
#         double_click = driver.find_element(By.XPATH, "//*[@ondblclick='myFunction1()']")
#         action = ActionChains(driver)
#         action.double_click(double_click).perform()
#         time.sleep(2)
#         x = driver.title
#         print(x)
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))


# unittest class method


class TestDoubleClickMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # cls.driver = webdriver.Chrome(executable_path="C:/selenium2/drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        URL = "https://testautomationpractice.blogspot.com/"
        cls.driver.get(URL)
        cls.driver.get_screenshot_as_file("C:/reports/file.png")

    def test_double_click_on_button(self):
        driver = self.driver
        double_click = driver.find_element(By.XPATH, "//*[@ondblclick='myFunction1()']")
        action = ActionChains(driver)
        action.double_click(double_click).perform()
        time.sleep(2)
        x = driver.title
        print(x)

    def test_drag_and_drop(self):
        driver = self.driver
        source = driver.find_element(By.XPATH, "//*[@id='draggable']")
        target = driver.find_element(By.XPATH, "//*[@id='droppable']")

        action = ActionChains(driver)
        action.drag_and_drop(source, target).perform()
        time.sleep(2)
        print(self.driver.title)
        self.assertTrue("Automation Testing Practice - Atom", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))






