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
# URL = "https://omayo.blogspot.com/"
# driver.get(URL)
# time.sleep(2)
# popup_link = driver.find_element("xpath", '//*[@id="HTML37"]/div[1]/p/a').click()
# whandle = driver.window_handles[1]
# driver.switch_to.window(whandle)
# print(driver.find_element("id","para1").text)
# time.sleep(1)
#
# driver.close()

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://omayo.blogspot.com/"
driver.get(URL)
time.sleep(2)
driver.execute_script("window.scrollBy(0,800);")
driver.execute_script("window.scrollBy(0,700);")
driver.find_element(By.XPATH, "//*[@id='HTML37']/div[1]/p/a").click()
print(driver.window_handles)
w_handle = driver.window_handles[1]
driver.switch_to.window(w_handle)
driver.get_screenshot_as_file("C:/reports/popupw.png")
print(driver.find_element(By.ID, "para1").text)
print(driver.find_element(By.ID, "para2").text)
time.sleep(2)

driver.close()

# headless mode

# chrome_options = Options()
# chrome_options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# URL = "https://omayo.blogspot.com/"
# driver.get(URL)
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,800);")
# driver.find_element(By.XPATH, "//*[@id='HTML37']/div[1]/p/a").click()
# popup_window = driver.window_handles[1]
# driver.switch_to.window(popup_window)
# time.sleep(2)
# print(driver.find_element(By.ID, "para1").text)
# print(driver.find_element(By.ID, "para2").text)
#
# driver.close()
# driver.quit()

'''
whandle = driver.window_handles[1] - this method gets the instance of the pop up window
driver.switch_to.window(whandle) - this method switches to the given pop-up window

https://www.educative.io/answers/how-to-handle-an-alert-and-pop-up-window-in-selenium-using-python
'''

# class TestSwitchToWindowHandle(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         URL = "https://omayo.blogspot.com/"
#         self.driver.get(URL)
#
#     def test_switch_to_pop_up_window(self):
#         driver = self.driver
#         driver.find_element(By.XPATH, "//*[@id='HTML37']/div[1]/p/a").click()
#         whandle = driver.window_handles[1]
#         driver.switch_to.window(whandle)
#         driver.get_screenshot_as_file("C:/reports/windowPopup.png")
#         time.sleep(2)
#         print(driver.find_element(By.ID, "para1").text)
#         print(driver.find_element(By.ID, "para2").text)
#
#
#     def tearDown(self):
#         self.driver.close()
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))