from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get("https://the-internet.herokuapp.com/context_menu")
a = driver.find_element(By.XPATH, "//*[@id='hot-spot']")
action = ActionChains(driver)
action.context_click(a).perform()

driver.quit()
