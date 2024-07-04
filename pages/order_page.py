import allure
from pages.base_page import BasePage
from selenium.webdriver import Keys
from locators.locators_main_page import LocatorsMainPage
from locators.locators_order_page import LocatorsOrderPage
from data_answer import DataAnswer


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
        self.fill_order_form(DataAnswer.ORDER_DATA_TOP_BUTTON)

    def fill_field_for_order_through_middle_button(self):
        self.enter_on_button(LocatorsMainPage.BUTTON_DOWN_ORDER)
        self.fill_order_form(DataAnswer.ORDER_DATA_MIDDLE_BUTTON)

    def fill_order_form(self, order_data):
        self.enter_text(LocatorsOrderPage.FIELD_FIRST_NAME, order_data["first_name"])
        self.enter_text(LocatorsOrderPage.FIELD_LAST_NAME, order_data["last_name"])
        self.enter_text(LocatorsOrderPage.FIELD_ADDRESS, order_data["address"])
        self.select_station(LocatorsOrderPage.FIELD_STATION)
        self.enter_text(LocatorsOrderPage.FIELD_PHONE_NUMBER, order_data["phone_number"])
        self.enter_on_button(LocatorsOrderPage.BUTTON_NEXT)

        self.select_current_date(LocatorsOrderPage.FIELD_DATE_DELIVERY)
        rental_value = getattr(LocatorsOrderPage, order_data["rental_value"])
        self.select_rental_period(LocatorsOrderPage.FIELD_RENTAL_PERIOD, rental_value)
        scooter_color = getattr(LocatorsOrderPage, order_data["scooter_color"])
        self.click_on_button(scooter_color)
        self.enter_text(LocatorsOrderPage.FIELD_COMMENT, order_data["comment"])
        self.enter_on_button(LocatorsOrderPage.BUTTON_ORDER_MIDDLE)
        self.enter_on_button(LocatorsOrderPage.BUTTON_ORDER_YES)
