import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/hovers")

a = driver.find_element(By.XPATH, "//div[@class='figure']/img")
action = ActionChains(driver)
action.move_to_element(a).perform()
time.sleep(2)
b = driver.find_element(By.XPATH, "//a[@href='/users/1']")
action.move_to_element(b).click().perform()
print(driver.find_element(By.XPATH, "//*[contains(text(),'Not Found')]").text)
time.sleep(2)

driver.quit()

# Headless mode

# chrome_options = Options()
# chrome_options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#
# driver.get("https://the-internet.herokuapp.com/hovers")
# a = driver.find_element(By.XPATH, "//div[@class='figure']/img")
# action = ActionChains(driver)
# action.move_to_element(a).perform()
# b = driver.find_element(By.XPATH, "//a[@href='/users/1']")
# action.move_to_element(b).click().perform()
# print(driver.find_element(By.XPATH, "//*[contains(text(),'Not Found')]").text)
#
# driver.quit()

# unittest

# class Test_HoverMoveToElementMethod(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver.implicitly_wait(10)
#         self.driver.get("https://the-internet.herokuapp.com/hovers")
#
#     def test_move_to_element(self):
#         driver = self.driver
#         a = driver.find_element(By.XPATH, "//div[@class='figure']/img")
#         action = ActionChains(driver)
#         action.move_to_element(a).perform()
#         b = driver.find_element(By.XPATH, "//a[@href='/users/1']")
#         action.move_to_element(b).click().perform()
#         time.sleep(5)
#         print(driver.find_element(By.XPATH, "//*[contains(text(),'Not Found')]"))
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))
#
