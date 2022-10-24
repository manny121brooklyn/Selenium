import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestGoogle():
    @pytest.fixture(scope="session")
    def test_setup_method(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()

        yield driver
        driver.quit()
        print("test completed")

    def test_opne_web(self, test_setup_method):
        # driver = self.driver
        driver.get("https://www.google.com")
        title = "Google"
        assert title == driver.title


    def test_search_for_word(self, test_setup_method):
        # driver = self.driver
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python tutorial")
        driver.find_element(By.NAME, "btnK").click()

    # def test_tear_down():
    #     driver.quit()




class TestGoogle():
    @pytest.fixture(scope="module")
    def test_setup_method(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()

        yield driver
        driver.quit()
        print("test completed")

    def test_opne_web(self, test_setup_method):
        # driver = self.driver
        driver.get("https://www.google.com")
        title = "Google"
        assert title == driver.title


    def test_search_for_word(self, test_setup_method):
        # driver = self.driver
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python tutorial")
        driver.find_element(By.NAME, "btnK").click()

    # def test_tear_down():
    #     driver.quit()




