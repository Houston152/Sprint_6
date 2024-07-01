from selenium.webdriver.common.by import By


class LocatorsMainPage:
    BUTTON_YANDEX = (By.XPATH, "//img[@alt='Yandex']")  # Кнопка "Яндекс"
    BUTTON_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")  # Кнопка "Самокат"
    BUTTON_UP_ORDER = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[contains(@class,'Button_Button')]")   # Верхняя кнопка "Заказать"
    BUTTON_DOWN_ORDER = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[contains(@class,'Button_Button')]")  # Нижняя кнопка "Заказать"
    DROP_DOWN_BUTTON_1 = (By.ID, "accordion__heading-0")
    ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    DROP_DOWN_BUTTON_2 = (By.ID, "accordion__heading-1")
    ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    DROP_DOWN_BUTTON_3 = (By.ID, "accordion__heading-2")
    ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    DROP_DOWN_BUTTON_4 = (By.ID, "accordion__heading-3")
    ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    DROP_DOWN_BUTTON_5 = (By.ID, "accordion__heading-4")
    ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    DROP_DOWN_BUTTON_6 = (By.ID, "accordion__heading-5")
    ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    DROP_DOWN_BUTTON_7 = (By.ID, "accordion__heading-6")
    ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    DROP_DOWN_BUTTON_8 = (By.ID, "accordion__heading-7")
    ANSWER_8 = (By.XPATH, "//div[@id='accordion__panel-7']/p")
    SECTION_WITH_QUESTIONS = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")
