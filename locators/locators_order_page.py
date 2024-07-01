from selenium.webdriver.common.by import By


class LocatorsOrderPage:
    YANDEX_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
    SCOOTER_BUTTON = (By.XPATH, "//img[@alt='Scooter']")

    FIELD_FIRST_NAME = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    FIELD_LAST_NAME = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")
    FIELD_ADDRESS = (By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]")
    FIELD_STATION = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]")
    FIELD_PHONE_NUMBER = (By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Далее')]")

    FIELD_DATE_DELIVERY = (By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]")
    FIELD_RENTAL_PERIOD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    RENTAL_VALUE_1 = (By.XPATH, "//div[contains(text(),'сутки')]")
    RENTAL_VALUE_2 = (By.XPATH, "//div[contains(text(),'двое суток')]")
    SCOOTER_BLACK = (By.ID, "black")
    SCOOTER_GREY = (By.ID, "grey")
    FIELD_COMMENT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]")
    BUTTON_ORDER_MIDDLE = (By.XPATH, "//button[contains(@class,'Button_Middle') and contains(text(),'Заказать')]")

    BUTTON_ORDER_YES = (By.XPATH, "//button[contains(text(),'Да')]")
    SUCCESS_ORDER = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")
