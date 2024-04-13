from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = By.XPATH, './/button[text()="Войти"]'
    EMAIL_FIELD = By.XPATH, './/input[@name="name"]'
    PASSWORD_FIELD = By.XPATH, './/input[@name="Пароль"]'
    ENTER_BUTTON = By.XPATH, './/h2[text()="Вход"]'
    PASSWORD_RECOVERY = By.XPATH, './/a[text()="Восстановить пароль"]'

