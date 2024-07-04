import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываю страницу приложения')
    def go_to_site(self, url):
        self.driver.get(url)

    @allure.step('Ищу элемент')
    def find_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not found {locator}')

    @allure.step('Нажимаю на элемент клавишей Enter')
    def enter_on_button(self, locator_button):
        self.driver.find_element(*locator_button).send_keys(Keys.ENTER)

    @allure.step('Нажимаю на элемент')
    def click_on_button(self, locator_button):
        self.driver.find_element(*locator_button).click()

    @allure.step('Получаю урл текущей вкладки')
    def check_current_url(self):
        return self.driver.current_url

    @allure.step('Получаю текст элемента')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Ввожу текст в поле')
    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)
