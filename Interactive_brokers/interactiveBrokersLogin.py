from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
print(driver.title)


try:
    driver.get("https://ndcdyn.interactivebrokers.com/sso/Login?RL=1&locale=en_US")
    username = driver.find_element(By.ID, "user_name")
    username.send_keys("mistas127")
    time.sleep(3)
    pwd = driver.find_element(By.ID, "password")
    pwd.send_keys("apBa2MHX")
    time.sleep(1)
    login_button = driver.find_element(By.ID, "submitForm")
    driver.execute_script("arguments[0]. click()", login_button)
    driver.get_screenshot_as_file("C:/reports/interactiverBrokers.png")

    time.sleep(2)
    trade_button = driver.find_element(By.XPATH, "//button[@class='_btn accent lg']")
    driver.execute_script("arguments[0].click()", trade_button)
    time.sleep(3)
    symbol_box = driver.find_element(By.XPATH, "//input[@id='cp-order-ticket-sl-input']")
    symbol_box.send_keys("AAPL")
    symbol_box.click()
    time.sleep(3)
    close_button = driver.find_element(By.XPATH, "//span[@class='fg50-inverse fs6 cursor  end-16']").click()
    time.sleep(3)
    welcome_button = driver.find_element(By.XPATH, "//div[@class='one-head-menu']/button")
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='ib-col flex inset-16']//button").click()
except Exception as e:
    print(e)

finally:
    driver.get_screenshot_as_file("C:/reports/close.png")
    driver.close()






