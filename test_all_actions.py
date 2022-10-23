import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class Test_AllItems(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get("https://testautomationpractice.blogspot.com/")

    def test_find_search_box(self):
        driver = self.driver
        search_box = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
        search_box.send_keys("wikipedia")
        search_box.submit()
        time.sleep(1)

    def test_switch_to_alert(self):
        driver = self.driver
        a = driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
        a = driver.switch_to.alert
        a.accept()
        time.sleep(2)
    #
    # def test_select_menu(self):
    #     driver = self.driver
    #     select_speed = driver.find_element(By.XPATH, "//select[@name='speed']")
    #     sel = Select(select_speed)
    #     sel.select_by_visible_text("Slower")
    #     time.sleep(2)
    #     sel.select_by_index(3)
    #     time.sleep(2)
    #
    # def test_select_a_file(self):
    #     driver = self.driver
    #     driver.execute_script("window.scrollBy(0,500);")
    #     sel = Select(driver.find_element(By.XPATH, "//select[@name='files']"))
    #     sel.select_by_index(1)
    #     time.sleep(2)
    #     sel.select_by_visible_text("DOC file")
    #     time.sleep(2)
    #
    # def test_select_a_number(self):
    #     driver = self.driver
    #     driver.execute_script("window.scrollBy(0,550);")
    #     number = driver.find_element(By.XPATH, "//select[@name='number']")
    #     sel = Select(number)
    #     sel.select_by_visible_text("3")
    #     time.sleep(2)
    #     sel.select_by_index(2)
    #     time.sleep(2)
    #
    # def test_select_a_product(self):
    #     driver = self.driver
    #     products = driver.find_element(By.XPATH, "//select[@name='products']")
    #     sel = Select(products)
    #     sel.select_by_visible_text("Yahoo")
    #     time.sleep(2)
    #     sel.select_by_index(3)
    #     time.sleep(2)
    #
    # def test_select_a_animal(self):
    #     driver = self.driver
    #     products = driver.find_element(By.XPATH, "//select[@name='animals']")
    #     sel = Select(products)
    #     sel.select_by_visible_text("Avatar")
    #     time.sleep(2)
    #     sel.select_by_index(2)
    #     time.sleep(2)
    #
    # def test_message_12(self):
    #     driver=self.driver
    #     # message_12 = driver.find_element(By.LINK_TEXT, "Message_12")
    #     message_12 = driver.find_element(By.XPATH, "//div[@class='widget-content']/span").is_displayed()
    #     driver.execute_script("window.scrollBy(0,550);")
    #     time.sleep(2)
    #     print(message_12)
    #     assert message_12 is True

    # def test_volunteer_signup(self):
    #     driver = self.driver
    #     driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='frame-one1434677811']"))
        # first_name = driver.find_element(By.XPATH, "//div[@id='q2']/input[@name='RESULT_TextField-1']")
        # first_name.send_keys("Michael")
        # time.sleep(2)

        # last_name = driver.find_element(By.XPATH, "//*[@name='RESULT_TextField-2']")
        # last_name.send_keys("Michaelson")
        # time.sleep(2)
        # phone = driver.find_element(By.NAME, "RESULT_TextField-3")
        # phone.send_keys("3478161616")
        # time.sleep(1)
        # country = driver.find_element(By.NAME, "RESULT_TextField-4")
        # country.send_keys("USA")
        # time.sleep(1)
        # city = driver.find_element(By.NAME, "RESULT_TextField-5")
        # city.send_keys("USA")
        # time.sleep(2)
        # email_address = driver.find_element(By.NAME, "RESULT_TextField-6")
        # email_address.send_keys("m.michaelson@gmail.com")
        # time.sleep(2)
        # driver.switch_to.default_content()

    # def test_check_radio_button(self):
    #     driver = self.driver
    #     driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='frame-one1434677811']"))
    #     driver.execute_script("window.scrollBy(0,500);")
    #     driver.find_element(By.XPATH, "//div[@id='q26']//input").click()
    #     # radio_button.click()
    #     time.sleep(2)
    #     # assert radio_button.is_enabled() is True



    # def test_click_on_checkbox(self):
    #     driver = self.driver
    #     driver.execute_script("window.scrollBy(1,500);")
    #
    #     driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='frame-one1434677811']"))
    #     checkbox = driver.find_element(By.XPATH, "//input[@id='RESULT_CheckBox-8_0']")
    #     checkbox.click()
    #     assert checkbox.is_enabled() is True
    #     time.sleep(2)
    #
    #     driver.switch_to.default_content()





    # def test_drag_and_drop(self):
    #     driver = self.driver
    #     source = driver.find_element(By.XPATH, "//div[@id='draggable']")
    #     target = driver.find_element(By.XPATH, "//div[@id='droppable']")
    #     action = ActionChains(driver)
    #     action.drag_and_drop(source, target).perform()
    #     time.sleep(2)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/reports"))


























# class Test_AllItems(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(ChromeDriverManager().install())
#         cls.driver.implicitly_wait(10)
#         cls.driver.get("https://testautomationpractice.blogspot.com/")
#
#     def test_find_search_box(self):
#         driver = self.driver
#         search_box = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
#         search_box.send_keys("wikipedia")
#         search_box.submit()
#         time.sleep(1)
#
#     def test_switch_to_alert(self):
#         driver = self.driver
#         a = driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
#         a = driver.switch_to.alert
#         a.accept()
#         time.sleep(2)
#
#     def test_select_menu(self):
#         driver = self.driver
#         driver.execute_script("window.scrollBy(0,500);")
#         select_speed = driver.find_element(By.XPATH, "//select[@name='speed']")
#         sel = Select(select_speed)
#         sel.select_by_visible_text("Slower")
#         time.sleep(2)
#         sel.select_by_index(3)
#         time.sleep(2)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()