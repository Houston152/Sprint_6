import allure
import pytest
from pages.main_page import MainPage
from locators.locators_main_page import LocatorsMainPage
from data_answer import DataAnswer
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCheckMainPage:

    @allure.description('Открываю вопрос и проверяю текст')
    @pytest.mark.parametrize('question,answer,answer_on_question',
                             [
                                 [LocatorsMainPage.DROP_DOWN_BUTTON_1, LocatorsMainPage.ANSWER_1, DataAnswer.answers_on_questions[0]],
                                 [LocatorsMainPage.DROP_DOWN_BUTTON_2, LocatorsMainPage.ANSWER_2, DataAnswer.answers_on_questions[1]],
                                 [LocatorsMainPage.DROP_DOWN_BUTTON_3, LocatorsMainPage.ANSWER_3, DataAnswer.answers_on_questions[2]],
                                 [LocatorsMainPage.DROP_DOWN_BUTTON_4, LocatorsMainPage.ANSWER_4, DataAnswer.answers_on_questions[3]],
                                 [LocatorsMainPage.DROP_DOWN_BUTTON_5, LocatorsMainPage.ANSWER_5, DataAnswer.answers_on_questions[4]],
                                 [LocatorsMainPage.DROP_DOWN_BUTTON_6, LocatorsMainPage.ANSWER_6, DataAnswer.answers_on_questions[5]],
                                 [LocatorsMainPage.DROP_DOWN_BUTTON_7, LocatorsMainPage.ANSWER_7, DataAnswer.answers_on_questions[6]],
                                 [LocatorsMainPage.DROP_DOWN_BUTTON_8, LocatorsMainPage.ANSWER_8, DataAnswer.answers_on_questions[7]]
                             ])
    def test_drop_down_answer(self, driver, question, answer, answer_on_question):
        ya_scooter_main_page = MainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.enter_on_button(question)
        ya_scooter_main_page.find_element(answer)
        assert ya_scooter_main_page.get_text(answer) == answer_on_question

    @allure.description('Перехожу на страницу яндекса и проверяю загрузку страницы')
    def test_go_to_yandex_page_through_yandex_button(self, driver):
        yandex_main_page = MainPage(driver)
        yandex_main_page.go_to_site(Urls.url_main_page)
        yandex_main_page.click_on_button_main_page()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 5).until(EC.url_to_be(Urls.url_yandex_page))
        expected_url = Urls.url_yandex_page
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Ожидалось, что URL будет '{expected_url}', но получил '{actual_url}'"
