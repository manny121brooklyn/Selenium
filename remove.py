from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.get("https://testautomationpractice.blogspot.com/")
#
# first_name = driver.find_element(By.NAME, "#RESULT_TextField-1")
# first_name.send_keys("hello")
# time.sleep(1)


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# # driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='frame-bottom']"))
#
# #
# # # driver.switch_to.default_content()
# # driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='frame-middle']"))
# # driver.switch_to.default_content()
# #
# checkbox = driver.find_element(By.XPATH, "//*[@type='checkbox']").click()
# # checkbox.is_enabled()
# time.sleep(2)
# # assert checkbox is True
# driver.quit()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/context_menu")
source = driver.find_element(By.XPATH, "//*[@id='hot-spot']").click()
action = ActionChains(driver)
action.context_click(source).perform()
time.sleep(10)
# alert = driver.switch_to.alert()
# alert.accept()

driver.quit()



