import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestContext(unittest.TestCase):

    custom_btn = (By.XPATH, '//*[@id="content"]/ul/li[7]/a')


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()

    def test2(self):
        self.driver.find_element(*self.custom_btn).click()
        ac = ActionChains(self.driver) # am creat un obiect
        ac.context_click(self.driver.find_element(By.ID, 'hot-spot')).perform() #click dreapta pe ceva
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
# TODO integrate try except in partea de alerta, dar sa aiba no alert present exception - se importa tot din .
    # daca odata avem odata nu avem o a;lerta se foloseste try except

    def tearDown(self) -> None:
        self.driver.quit()