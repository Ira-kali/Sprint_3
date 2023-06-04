import pytest
from selenium import webdriver

url = 'https://stellarburgers.nomoreparties.site'

@pytest.fixture(scope="function", autouse=True)
def driver():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()
