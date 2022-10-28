import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

# class TestGoogle():

# @pytest.fixture(scope="class")
# def browser():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#
#     yield driver
#     driver.quit()
#
# def test_google_site(browser):
#     try:
#         driver=browser
#         driver.get("https://www.google.com")
#         driver.find_element(By.NAME, "q").send_keys("jenkins")
#         element = driver.find_element(By.NAME, "btnK")
#         element.click()
#         assert "Google" == driver.title
#
#     except Exception as e:
#         print(e)
#     finally:
#         driver.close()


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

def test_google_site(browser):
    try:

        browser.get("https://www.google.com")
        browser.find_element(By.NAME, "q").send_keys("jenkins")
        element = browser.find_element(By.NAME, "btnK")
        browser.execute_script("arguments[0].click()", element)
        # element.click()
        assert "Google" == browser.title

    except Exception as e:
        print(e)
    finally:
        browser.get_screenshot_as_file("C:/reports/google.gif")
        # browser.save_screenshot("google1.gif")
        browser.close()
