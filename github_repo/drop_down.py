from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.get("https://testautomationpractice.blogspot.com")
# print('test has begun')
# driver.execute_script("window.scrollBy(0,500);")
# txt_drp = driver.find_element(By.NAME, "files")
# sel = Select(txt_drp)
# sel.select_by_index(3)
# time.sleep(2)
# sel.select_by_visible_text("DOC file")
# time.sleep(2)
# print("test finished")
#
# driver.quit()

# click using JavaScript script click()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Python course")
time.sleep(2)
driver.find_element(By.NAME, "btnK")
# driver.execute_script("arguments[0].click();", element)
driver.execute_script("arguments[0].click();", driver.find_element(By.NAME, "btnK"))

driver.quit()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Python course")
time.sleep(2)
element = driver.find_element(By.NAME, "btnK")
driver.execute_script("arguments[0].click();", element)


driver.quit()
