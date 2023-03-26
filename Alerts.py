import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):

    alert_page_js = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
    alert_page_confirm = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
    alert_page_prompyt = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
    btn_alerts = (By.XPATH, '//*[@id="content"]/ul/li[29]/a')



    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()

    def test3(self):
        self.driver.find_element(*self.btn_alerts).click()
        self.driver.find_element(*self.alert_page_js).click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(*self.alert_page_confirm).click()
        self.driver.switch_to.alert.dismiss()
        self.driver.find_element(*self.alert_page_prompyt).click()
        my_input = 'hehe'
        self.driver.switch_to.alert.send_keys(my_input)
        self.driver.switch_to.alert.accept()
        assert my_input in self.driver.find_element(By.ID, 'result').text
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()