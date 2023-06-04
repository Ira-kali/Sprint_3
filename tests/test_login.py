from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestLogin():
    def test_login_by_clicking_login_button(self, driver): #вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        checkout = driver.find_element(*Locators.CHECKOUT).text
        assert checkout == 'Оформить заказ'

    def test_login_personal_account_button(self, driver): #вход через кнопку «Личный кабинет»
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        checkout = driver.find_element(*Locators.CHECKOUT).text
        assert checkout == 'Оформить заказ'

    def test_login_button_registration_form(self, driver): #вход через кнопку в форме регистрации
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys('Irina')
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_899@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REGISTR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        checkout = driver.find_element(*Locators.CHECKOUT).text
        assert checkout == 'Оформить заказ'

    def test_login_password_recovery_button(self,driver): # вход через кнопку в форме восстановления пароля
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.PASS_RECOVERY_BUTTON).click()
        driver.find_element(*Locators.RESTORE_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('ira_kalinina_10_111@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECKOUT))
        checkout = driver.find_element(*Locators.CHECKOUT).text
        assert checkout == 'Оформить заказ'





