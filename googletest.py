from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# # driver = webdriver.Chrome(executable_path="C://selenium2//chromedriver.exe")
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.google.com")
# driver.find_element_by_name("q").send_keys("Python tutorials")
# driver.find_element_by_name("btnK")
# time.sleep(3)
#
#
#
#
#
# driver.quit()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")

dr = driver.find_element(By.NAME, "q")

dr.send_keys("Python tutorial")
dr.click()
# dr.send_keys(Keys.RETURN)
# dr.submit()
time.sleep(2)


# send_keys(Keys.RETURN)
# click search button
# driver.find_element(By.NAME, "btnK").click()
# time.sleep(2)

driver.quit()
