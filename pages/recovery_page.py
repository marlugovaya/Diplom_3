import allure

from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):

    recovery_url = 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.step('Кликаем на кнопку восстановления пароля')
    def recovery_button_click(self):
        self.click_on_element(RecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Заполняем поле Email')
    def set_email_field(self, email):
        self.get_element_set_text(RecoveryPageLocators.EMAIL_FIELD, email)

    @allure.step('Получаем значение Email')
    def get_email(self):
        return self.get_element(RecoveryPageLocators.EMAIL_FIELD).get_attribute('value')

    @allure.step('Кликаем на иконку с глазом')
    def eye_icon_click(self):
        self.click_on_element(RecoveryPageLocators.EYE_ICON)