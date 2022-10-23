import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class TestRightClick(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.tutorialspoint.com/about/about_careers.htm")

    def test_right_click_on_object(self):
        driver = self.driver
        driver.refresh()
        source = driver.find_element(By.XPATH, "//*[text()='Company']")
        action = ActionChains(driver)
        action.context_click(source).perform()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))
