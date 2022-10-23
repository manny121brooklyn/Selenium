from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
URL = "https://www.python.org"
driver.get(URL)
time.sleep(3)
# driver.execute_script("window.scrollBy(0,500);")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.save_screenshot('screenshot2.png')
# driver.get_screenshot_as_file("screenshot3.png")
# driver.execute_script("window.scrollBy(0,500)")
# driver.execute_script("return document.body.scrollHeight")
label = driver.find_element(By.XPATH, "//*[contains(text(),'Become a Member')]")
label.location_once_scrolled_into_view
# label = driver.send_keys(Keys.PAGE_DOWN)

driver.quit()
