import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
import unittest

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

class TestDragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    def test_drag_and_drop(self):
        driver = self.driver
        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.ID, "column-b")
        action = ActionChains(driver)
        action.drag_and_drop(source, target).perform()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




