import time

import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

actions = ActionChains(driver)
source = driver.find_element(By.ID, "box3")
target = driver.find_element(By.ID, "box103")
actions.drag_and_drop(source, target).perform()
time.sleep(2)

source = driver.find_element(By.ID, "box6")
target = driver.find_element(By.ID, "box106")
actions.drag_and_drop(source, target).perform()
time.sleep(2)

source = driver.find_element(By.ID, "box1")
target = driver.find_element(By.ID, "box101")
actions.drag_and_drop(source, target).perform()
time.sleep(2)

source = driver.find_element(By.ID, "box4")
target = driver.find_element(By.ID, "box104")
actions.drag_and_drop(source, target).perform()
time.sleep(2)

source = driver.find_element(By.ID, "box7")
target = driver.find_element(By.ID, "box107")
actions.drag_and_drop(source, target).perform()
time.sleep(2)

source = driver.find_element(By.ID, "box5")
target = driver.find_element(By.ID, "box105")
actions.drag_and_drop(source, target).perform()
time.sleep(2)

source = driver.find_element(By.ID, "box2")
target = driver.find_element(By.ID, "box102")
actions.drag_and_drop(source, target).perform()
time.sleep(2)


driver.quit()

'''
hello
'''