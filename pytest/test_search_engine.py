import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select

class TestSearchEngine:

    # @pytest.fixture(scope="module")
    def browser(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path="C:/selenium2/drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print(self.driver.title)
        print(self.driver.current_url)
        URL = "https://www.google.com"
        self.driver.get(URL)

        yield
        self.driver.quit()

    def test_search_engine_for_phrase(self, browser):
        driver = self.driver
        search = driver.find_element(By.NAME, "q")
        search.send_keys('pytest bdd')
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        title = "Google"
        assert title == driver.title

