from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.geeksforgeeks.org/")
# element = driver.find_element(By.LINK_TEXT, "Courses")
# time.sleep(2)
# action = ActionChains(driver)
# action.click(on_element=element)
# action.perform()
# time.sleep(2)
#
# driver.quit()

# Example 2

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

log_btn = driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

driver.quit()

# not complete