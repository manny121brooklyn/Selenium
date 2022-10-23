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
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.LINK_TEXT, "Frames").click()
# time.sleep(1)
# driver.find_element(By.LINK_TEXT, "Nested Frames").click()
# time.sleep(1)
# # switch to frame Bottom
# driver.switch_to.frame("frame-bottom")
# txt = driver.find_element(By.XPATH, "//*[contains(text(),'BOTTOM')]").text
# print(txt)
# driver.switch_to.default_content()
#
# driver.quit()

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.LINK_TEXT, "Frames").click()
# time.sleep(1)
# driver.find_element(By.LINK_TEXT, "Nested Frames").click()
# time.sleep(1)
# # driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='frame-left']"))
# driver.switch_to.frame("frame-middle")
# left_frame= driver.find_element(By.XPATH, "//*[contains(text(),'MIDDLE')]").text
# print(left_frame)
# driver.switch_to.default_content()
#
# driver.quit()


# --------------------------- Unittest method ---------------------------------------------

# class TestSwitchToFrame(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver.implicitly_wait(10)
#         self.driver.get("https://the-internet.herokuapp.com/")
#         self.driver.find_element(By.LINK_TEXT, "Frames").click()
#         self.driver.find_element(By.LINK_TEXT, "Nested Frames").click()
#
#     def test_switch_to_bottom_frame(self):
#         driver = self.driver
#         driver.switch_to.frame("frame-bottom")
#         txt = driver.find_element(By.XPATH, "//*[contains(text(),'BOTTOM')]").text
#         print(txt)
#         driver.switch_to.default_options()

#
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()

# -------------------------Headless mode--------------------------------

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT, "Frames").click()
# time.sleep(1)
driver.find_element(By.LINK_TEXT, "Nested Frames").click()
# time.sleep(1)
# driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='frame-left']"))
driver.switch_to.frame("frame-bottom")
left_frame= driver.find_element(By.XPATH, "//*[contains(text(),'BOTTOM')]").text
print(left_frame)
driver.switch_to.default_content()

driver.quit()