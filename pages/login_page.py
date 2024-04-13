import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    login_url = 'https://stellarburgers.nomoreparties.site/login'

    @allure.step("Авторизуемся")
    def log_in_account(self, user):
        self.set_email_text(user['email'])
        self.set_password_text(user['password'])
        self.login_button_click()

    @allure.step('Заполняем поле Email')
    def set_email_text(self, email):
        self.get_element_set_text(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Заполняем поле Пароль')
    def set_password_text(self, password):
        self.get_element_set_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Кликаем на кнопку Войти')
    def login_button_click(self):
        self.get_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Кликаем на кнопку восстановления пароля')
    def password_recovery_click(self):
        self.get_element(LoginPageLocators.PASSWORD_RECOVERY).click()

