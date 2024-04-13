from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    PASSWORD_RECOVERY_BUTTON = By.XPATH, './/button[text()="Восстановить"]'
    EMAIL_FIELD = By.XPATH, '//input[@name="name"]'
    PASSWORD = By.XPATH, './/label[text()="Пароль"]'
    EYE_ICON = By.CLASS_NAME, 'input__icon'
    SAVE_BUTTON = By.XPATH, './/button[text()="Сохранить"]'
    RECOVERY_HEADER = By.XPATH, './/h2[text()="Восстановление пароля"]'
