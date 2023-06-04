from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class TestPersonalAccount():
    def test_go_personal_account(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))
        profile = driver.find_element(*Locators.PROFILE).text
        assert profile == 'Профиль'
