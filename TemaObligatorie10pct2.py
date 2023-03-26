# emag.ro
''' 2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
'''

import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class TestTema10(unittest.TestCase):
    oferta_zilei = (By.XPATH, '//*[@id="auxiliary"]/div/div/ul[2]/li[3]/a')
    cookie_pag1 = (By.CLASS_NAME, 'btn btn-primary js-accept gtm_h76e8zjgoo btn-block')
    extra = (By.XPATH, "//section[@id='cp_widget_54663']//div[@class='container']//div[1]//span[1]")
    CLOSE = (By.XPATH, "//button[@class='js-dismiss-login-notice-btn dismiss-btn btn btn-link pad-sep-none pad-hrz-none']//i[@class='em em-close']")
    fashion = (By.XPATH, "//span[normalize-space()='Fashion']")
    genti = (By.XPATH, "//a[normalize-space()='Genti si accesorii femei']")
    genti_dama = (By.XPATH, "//ul[@class='emg-aside-links']//a[contains(text(),'Genti dama')]")
    card_milioane = (By.XPATH, "//a[normalize-space()='Cardul cu milioane de idei']")
    continua = (By.XPATH, "//button[@class='section-button section-change-button themes-section-button']")
    valoare_card = (By.XPATH, '//*[@id="main-container"]/div[1]/form/div[3]/div[2]/a[2]')
    continua_card = (By.XPATH, '//*[@id="main-container"]/div[1]/form/div[1]/button')
    nume = (By.XPATH, '//*[@id="recipient-name"]')


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.emag.ro/')
        self.driver.maximize_window()

    def test_oferta_zilei(self):
        self.driver.find_element(*self.oferta_zilei).click()
        time.sleep(3)
        # self.driver.find_element(*self.CLOSE).click()
        # time.sleep(2)
        try:
            self.driver.find_element(*self.cookie_pag1).click()
        except NoSuchElementException:
            print('Cookies not found')
        msg = self.driver.find_element(By.XPATH, "//div[@class='cp-banner-container']//div[@class='relative inline-block hotspots-container without-image']").text
        assert msg in "Oferta zilei"

    def test_link_genti_dama(self):

        self.driver.find_element(*self.fashion).click()
        self.driver.find_element(*self.genti).click()
        self.driver.find_element(*self.genti_dama).click()
        curent_url = self.driver.current_url
        actual_url = 'https://www.emag.ro/genti-dama/c?tree_ref=1734&ref=cat_tree_2362'
        self.assertTrue(actual_url, curent_url)

    def test_cardul_milioane_blocked_by_cookie(self):
        self.driver.find_element(*self.card_milioane).click()
        self.driver.find_element(*self.continua).click()
        self.driver.find_element(*self.valoare_card).click()
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'blocked':
                self.skipTest("Skipping test since site is blocking testing by setting a 'blocked' cookie")

        # self.driver.find_element(*self.nume).send_keys('Andreea')
        # self.driver.find_element(By.ID, 'recipient-email').send_keys('deeacara@gmail.com')
        # self.driver.find_element(By.ID, 'recipient-email-confirm').send_keys('deeacara@gmail.com')
        # self.driver.find_element(By.ID, 'sender-name').send_keys('Mihaela')
        # self.driver.find_element(By.ID, 'sender-message').send_keys('Love you')
        # self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-emag.gift-card-add-to-cart-button').click()
        # msg = (By.CSS_SELECTOR, 'order-summary-title')
        # assert msg == 'Sumar comanda'


    def tearDown(self) -> None:
        self.driver.quit()
