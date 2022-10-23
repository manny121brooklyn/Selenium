import time
#
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
# driver = webdriver.Chrome(executable_path="C:/selenium2/drivers/chromedriver.exe")
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
driver.execute_script("window.scrollBy(0,800);")
# drop_down = driver.find_element(By.NAME, "continents")
drop_down = driver.find_element(By.XPATH, "//select[@name='continents']")
sel = Select(drop_down)

sel.select_by_visible_text("South America")
time.sleep(2)
sel.select_by_index(0)
time.sleep(2)

driver.quit()



# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# # driver = webdriver.Chrome(executable_path="C:/selenium2/drivers/chromedriver.exe")
# driver.implicitly_wait(0.5)
# driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# # identify dropdown with Select class
# sel = Select(driver.find_elements(By.XPATH, "//select[@name='continents']"))
# #select by select_by_visible_text() method
# sel.select_by_visible_text("Europe")
# time.sleep(0.8)
# #select by select_by_index() method
# sel.select_by_index(0)
# driver.close()


