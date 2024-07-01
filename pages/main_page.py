import allure
from locators.locators_main_page import LocatorsMainPage
from locators.locators_yandex_main_page import LocatorYandexMainPage
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_button_main_page(self):
        self.click_on_button(LocatorsMainPage.BUTTON_YANDEX)

    @allure.step('Получаю текст элемента')
    def get_text_main_page(self):
        return self.get_text(LocatorYandexMainPage.HEADER_YANDEX_MAIN_PAGE)
