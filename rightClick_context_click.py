from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.get("https://the-internet.herokuapp.com/context_menu")
# a = driver.find_element(By.XPATH, "//*[@id='hot-spot']")
#
# # create action chain object
# # context_click(args) - performs right click operation on an element of the page
# # args is the element that has to be right clicked
# action = ActionChains(driver)
# action.context_click(a).perform()
# time.sleep(2)
#
# driver.quit()


chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get("https://the-internet.herokuapp.com/context_menu")
a = driver.find_element(By.XPATH, "//*[@id='hot-spot']")
action = ActionChains(driver)
action.context_click().perform()

driver.quit()

