
import allure

from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.account_page import AccountPage
from pages.login_page import LoginPage


class TestAccountPage:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_move_to_account(self, driver, user, login):
        account_page = AccountPage(driver)
        account_page.account_button_click()

        assert 'Профиль' in account_page.get_text_from_element(AccountPageLocators.PROFILE)

    @allure.title('Переход в раздел «История заказов»')
    def test_move_to_order_history(self, driver, user, login):
        account_page = AccountPage(driver)
        account_page.account_button_click()
        account_page.history_click()
        current_url = account_page.driver.current_url

        assert current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, user, login):
        account_page = AccountPage(driver)
        account_page.account_button_click()
        account_page.exit_click()
        login_page = LoginPage(driver)

        assert 'Вход' in login_page.get_text_from_element(LoginPageLocators.ENTER_BUTTON)

