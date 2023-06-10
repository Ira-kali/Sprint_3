from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class TestDesigner():
    def test_bun(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.BUNS).click()
        buns = driver.find_element(*Locators.BUN_R2_D3).text
        assert buns == 'Флюоресцентная булка R2-D3'


    def test_sauces(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        driver.find_element(*Locators.SAUCES).click()
        sauces = driver.find_element(*Locators.SAUCE_GALAXY).text
        assert sauces == 'Соус традиционный галактический'

    def test_fillings(self,driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        driver.find_element(*Locators.FILLINGS).click()
        fillings = driver.find_element(*Locators.FILLING_CHEESE).text
        assert fillings == 'Сыр с астероидной плесенью'
