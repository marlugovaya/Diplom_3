import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://stellarburgers.nomoreparties.site/'

    @allure.step('Открываем страницу')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Получаем элемент')
    def get_element(self, locator):
        element = self.wait_for_element_visibility(locator)
        self.scroll_to_element(element)
        return self.driver.find_element(*locator)

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидаем элемент')
    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидаем исчезновения элемента')
    def wait_for_element_invisibility(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        self.get_element(locator).click()

    @allure.step('Задаем текст элементу')
    def get_element_set_text(self, locator, text):
        self.get_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.get_element(locator).text

    @allure.step('Перетаскиваем ингредиент в бургер')
    def drag_and_drop_element(self, driver, locator_from, locator_to):
        action_chains = ActionChains(driver)
        element_from = self.get_element(locator_from)
        element_to = self.get_element(locator_to)
        action_chains.drag_and_drop(element_from, element_to).perform()