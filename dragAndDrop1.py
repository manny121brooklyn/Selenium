import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
#
# source = driver.find_element(By.ID, "column-a")
# target = driver.find_element(By.ID, "column-b")
#
# action = ActionChains(driver)
# action.drag_and_drop(source, target).perform()
# time.sleep(2)
#
# driver.refresh()
# source1 = driver.find_element(By.ID, "column-b")
# target1 = driver.find_element(By.ID, "column-a")
#
# action = ActionChains(driver)
# action.drag_and_drop(source1, target1).perform()
# time.sleep(2)
#
# driver.quit()


# headless mode

# from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
print('Headless mode initialized')
source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
print("Some action happened here ...")
print("Headless mode test complete")

driver.quit()