from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestRegistration():
        def test_registration_success(self, driver):
                driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
                driver.find_element(*Locators.REG_BUTTON).click()
                name = driver.find_element(*Locators.NAME)
                name.send_keys('Irina')
                driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_676@mail.ru')
                driver.find_element(*Locators.PASSWORD).send_keys('123456')
                driver.find_element(*Locators.REGISTR_BUTTON).click()
                WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.TITLE))
                assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', 'Не успешная регистрация пользователя'

        def test_register_incorrect_password(self, driver):
                driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
                driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_555@mail.ru')
                driver.find_element(*Locators.PASSWORD).send_keys('123')
                driver.find_element(*Locators.LOGIN_BUTTON).click()
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))
                error_text = driver.find_element(*Locators.ERROR_TEXT).text
                assert error_text == 'Некорректный пароль'
