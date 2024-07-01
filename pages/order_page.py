import allure
from pages.base_page import BasePage
from selenium.webdriver import Keys
from locators.locators_main_page import LocatorsMainPage
from locators.locators_order_page import LocatorsOrderPage


class ScooterOrderPage(BasePage):

    @allure.step('Выбираю станцию метро')
    def select_station(self, locator):
        a = self.driver.find_element(*locator)
        a.click()
        a.send_keys(Keys.DOWN)
        a.send_keys(Keys.ENTER)

    @allure.step('Выбираю текущую дату')
    def select_current_date(self, locator):
        a = self.driver.find_element(*locator)
        a.click()
        a.send_keys(Keys.ENTER)

    @allure.step('Выбираю срок использования')
    def select_rental_period(self, locator, period_value):
        self.driver.find_element(*locator).click()
        self.driver.find_element(*period_value).click()

    def get_text_successful_order(self):
        return self.get_text(LocatorsOrderPage.SUCCESS_ORDER)

    def get_text_block_with_questions(self):
        return self.get_text(LocatorsMainPage.SECTION_WITH_QUESTIONS)

    def enter_on_button_order_in_header(self):
        self.enter_on_button(LocatorsMainPage.BUTTON_UP_ORDER)

    def click_on_button_scooter(self):
        self.click_on_button(LocatorsOrderPage.SCOOTER_BUTTON)

    def fill_field_for_order_through_top_button(self):
        self.enter_on_button_order_in_header()
        self.enter_text(LocatorsOrderPage.FIELD_FIRST_NAME, "Иван")
        self.enter_text(LocatorsOrderPage.FIELD_LAST_NAME, "Иванов")
        self.enter_text(LocatorsOrderPage.FIELD_ADDRESS, "г. Нижний Новгород, д. 1")
        self.select_station(LocatorsOrderPage.FIELD_STATION)
        self.enter_text(LocatorsOrderPage.FIELD_PHONE_NUMBER, "+71111111111")
        self.enter_on_button(LocatorsOrderPage.BUTTON_NEXT)

        self.select_current_date(LocatorsOrderPage.FIELD_DATE_DELIVERY)
        self.select_rental_period(LocatorsOrderPage.FIELD_RENTAL_PERIOD, LocatorsOrderPage.RENTAL_VALUE_1)
        self.click_on_button(LocatorsOrderPage.SCOOTER_BLACK)
        self.enter_text(LocatorsOrderPage.FIELD_COMMENT, "Не торопитесь привозить")
        self.enter_on_button(LocatorsOrderPage.BUTTON_ORDER_MIDDLE)
        self.enter_on_button(LocatorsOrderPage.BUTTON_ORDER_YES)


    def fill_field_for_order_through_middle_button(self):
        self.enter_on_button(LocatorsMainPage.BUTTON_DOWN_ORDER)
        self.enter_text(LocatorsOrderPage.FIELD_FIRST_NAME, "Петр")
        self.enter_text(LocatorsOrderPage.FIELD_LAST_NAME, "Петров")
        self.enter_text(LocatorsOrderPage.FIELD_ADDRESS, "г. Москва, д. 2")
        self.select_station(LocatorsOrderPage.FIELD_STATION)
        self.enter_text(LocatorsOrderPage.FIELD_PHONE_NUMBER, "+72222222222")
        self.enter_on_button(LocatorsOrderPage.BUTTON_NEXT)

        self.select_current_date(LocatorsOrderPage.FIELD_DATE_DELIVERY)
        self.select_rental_period(LocatorsOrderPage.FIELD_RENTAL_PERIOD, LocatorsOrderPage.RENTAL_VALUE_2)
        self.click_on_button(LocatorsOrderPage.SCOOTER_GREY)
        self.enter_text(LocatorsOrderPage.FIELD_COMMENT, "Самокат очень срочно нужен")
        self.enter_on_button(LocatorsOrderPage.BUTTON_ORDER_MIDDLE)
        self.enter_on_button(LocatorsOrderPage.BUTTON_ORDER_YES)
