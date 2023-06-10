from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT = (By.XPATH, "//a[@href = '/account']") # Кнопка "Личный кабинет"
    REG_BUTTON = (By.XPATH, "//a[@href='/register']") # Кнопка "Зарегистрироваться" в личном кабинете
    NAME = (By.XPATH, "//label[text() = 'Имя']/parent::div/input") # Поле "Имя" в окне регистрации
    EMAIL = (By.XPATH, "//label[text() = 'Email']/parent::div/input") # Email
    PASSWORD = (By.XPATH, "//input[@name='Пароль']") # Пароль
    REGISTR_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться" в окне регистрации
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # Кнопка "Войти" на странице
    TITLE = (By.XPATH, "//h2[contains(text(),'Вход')]") # Заголовок Вход
    ERROR_TEXT = (By.XPATH, "//p[@class='input__error text_type_main-default']") # Сообщение "Неверный пароль"
    ACCOUNT_BUTTON = (By.XPATH, "// button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    CHECKOUT = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    PASS_RECOVERY_BUTTON = (By.XPATH, "//a[@href = '/forgot-password']") # Кнопка "Восстановить пароль"
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]") # Кнопка "Восстановить"
    RESTORE_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]") # Кнопка "Войти" в форме восстановления пароля
    PROFILE = (By.XPATH, "//a[text()='Профиль']") # Заголовок "Профиль"
    DESIGNER = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # Логотип
    LOGOUT = (By.XPATH, "//button[text() = 'Выход']") # Кнопка "Выход"
    BUNS = (By.XPATH, "//span[contains(text(),'Булки')]") # Раздел "Булки"
    SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]") # Раздел  "Соусы"
    FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]") # Раздел "Начинки"
    BUN_R2_D3 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']") # Флюоресцентная булка R2-D3
    SAUCE_GALAXY = (By.XPATH, "//p[text()='Соус традиционный галактический']") # Соус традиционный галактический
    FILLING_CHEESE = (By.XPATH, "//p[text()='Сыр с астероидной плесенью']") # Сыр с астероидной плесенью
    TEXT_INPUT = (By.XPATH, "//h2[text()='Вход']") # Текст "Вход"
    ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']") # Текст "Соберите бургер"
    HISTORY_ORDERS = (By.XPATH, "//a[text()='История заказов']") # Заголовок "История заказов"
