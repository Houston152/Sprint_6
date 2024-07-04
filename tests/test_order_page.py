import allure
from locators.locators_main_page import LocatorsMainPage
from locators.locators_order_page import LocatorsOrderPage
from pages.order_page import ScooterOrderPage
from urls import Urls


class TestCreateOrder:

    @allure.description('Оформляю заказ через верхнюю кнопку и проверяю, что заказ оформился')
    def test_order_through_top_button(self, driver):
        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.url_main_page)
        scooter_order_page.fill_field_for_order_through_top_button()

        assert "Заказ оформлен" in scooter_order_page.get_text_successful_order()

    @allure.description('Оформляю заказ через среднюю кнопку и проверяю, что заказ оформился')
    def test_order_through_middle_button(self, driver):
        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.url_main_page)
        scooter_order_page.fill_field_for_order_through_middle_button()

        assert "Заказ оформлен" in scooter_order_page.get_text_successful_order()

    @allure.description('Проверяю, что по нажатию на кнопку "Самокат" открывается главная страница')
    def test_go_to_main_page_through_scooter_button(self, driver):
        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.url_main_page)
        scooter_order_page.enter_on_button_order_in_header()
        scooter_order_page.click_on_button_scooter()

        assert scooter_order_page.get_text_block_with_questions() == "Вопросы о важном"
