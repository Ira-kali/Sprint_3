from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class TestPersonalAccountToDesigner():
    def test_personal_account_click_on_constructor(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.DESIGNER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        checkout = driver.find_element(*Locators.CHECKOUT).text
        assert checkout == 'Оформить заказ'

    def test_personal_account_click_on_logo(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        checkout = driver.find_element(*Locators.CHECKOUT).text
        assert checkout == 'Оформить заказ'
