
import allure

from locators.recovery_page_locators import RecoveryPageLocators
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage


class TestRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»,')
    def test_move_to_password_recovery(self, driver, user):
        login_page = LoginPage(driver)
        login_page.open_url(login_page.login_url)
        login_page.password_recovery_click()
        recovery_page = RecoveryPage(driver)
        recovery_page.set_email_field(user['email'])

        assert recovery_page.get_email() == user['email']

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_set_email_click_on_recover(self, driver, user):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_url(recovery_page.recovery_url)
        recovery_page.set_email_field(user['email'])
        recovery_page.recovery_button_click()

        assert 'Восстановление пароля' in recovery_page.get_text_from_element(RecoveryPageLocators.RECOVERY_HEADER)

    @allure.title('Клик на иконку показать/скрыть пароль делает поле активным')
    def test_show_hide_password(self, driver, user):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_url(recovery_page.recovery_url)
        recovery_page.set_email_field(user)
        recovery_page.recovery_button_click()
        recovery_page.eye_icon_click()

        assert 'input__placeholder-focused' in recovery_page.wait_for_element_visibility(RecoveryPageLocators.PASSWORD).get_attribute('class')
