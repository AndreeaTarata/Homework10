# 1.  https://www.techlistic.com/p/selenium-practice-form.html
''' 2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
'''

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestTema10(unittest.TestCase):
    cookies = (By.ID, 'ez-accept-all')
    first_name = (By.NAME, 'firstname')
    last_name = (By.NAME, 'lastname')
    gender = (By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[9]')
    male = (By.ID, "sex-0")
    year_of_experience = (By.ID, 'exp-0')
    date = (By.ID, 'datepicker')
    professiona = (By.ID, 'profession-1')
    automation_toll = (By.ID, 'tool-2')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
        self.driver.maximize_window()

    def test_signup(self):
        self.driver.find_element(*self.cookies).click()

        self.driver.find_element(*self.first_name).send_keys('Andreea')
        self.driver.find_element(*self.last_name).send_keys('Deea')
        self.driver.find_element(*self.male).click()
        self.driver.find_element(*self.year_of_experience).send_keys('21.03.2021')
        self.driver.find_element(*self.professiona).click()
        self.driver.find_element(*self.automation_toll).click()
        continents = Select(self.driver.find_element(By.ID, 'Continents'))
        continents.select_by_visible_text("Australia")
        time.sleep(7)
        selenium_comandas = Select(self.driver.find_element(By.ID, 'selenium_commands'))
        selenium_comandas.select_by_visible_text("Wait Commands")
        upload_image = (By.ID, 'photo')
        btn = (By.ID, "submit")
        self.driver.find_element(*self.btn).send_keys("C:\Users\andre\Pictures\Screenshots\Screenshot 2023-03-12 184838.png")



    def tearDown(self) -> None:
        self.driver.quit())
