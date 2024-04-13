from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_BUTTON = By.XPATH, './/p[text()="Личный Кабинет"]'
    PROFILE = By.XPATH, './/a[text()="Профиль"]'
    HISTORY = By.XPATH, './/a[text()="История заказов"]'
    EXIT = By.XPATH, './/button[text()="Выход"]'


