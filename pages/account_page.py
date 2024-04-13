import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Кликаем на кнопку Личный кабинет')
    def account_button_click(self):
        self.click_on_element(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step('Кликаем на кнопку История заказов')
    def history_click(self):
        self.click_on_element(AccountPageLocators.HISTORY)

    @allure.step('Кликаем на кнопку Выход')
    def exit_click(self):
        self.click_on_element(AccountPageLocators.EXIT)
