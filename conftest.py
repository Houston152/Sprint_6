import allure
import pytest
from selenium import webdriver


@allure.step('Открываю браузер')
@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
