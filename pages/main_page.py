
import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликаем на Конструктор')
    def click_on_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем на Ленту заказов')
    def click_on_feed(self):
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step('Закрываем ингредиент кликом по крестику')
    def click_on_cross(self):
        self.click_on_element(MainPageLocators.CROSS_BUTTON)

    @allure.step('Добавляем заданное количество ингредиентов в бургер')
    def add_ingredients(self, driver, count):
        for i in range(count):
            from_ingredients = MainPageLocators.INGREDIENT
            to_burger = MainPageLocators.CONSTRUCTOR_BASKET
            self.drag_and_drop_element(driver, from_ingredients, to_burger)

    @allure.step('Добавляем булку в бургер')
    def add_bun(self, driver):
        from_buns = MainPageLocators.BUN
        to_burger = MainPageLocators.CONSTRUCTOR_BASKET
        self.drag_and_drop_element(driver, from_buns, to_burger)

    @allure.step('Кликаем на Оформить заказ')
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Ожидаем, пока дефолтный 9999 поменяется на номер заказа')
    def wait_order_number_change(self):
        self.wait_for_element_invisibility(MainPageLocators.DEFAULT_ORDER_NUMBER)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        return str(self.get_text_from_element(MainPageLocators.ORDER_NUMBER))

    @allure.step('Получаем количество ингредиентов в бургере')
    def get_ingredients_count(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNT)

    @allure.step('Собираем бургер и нажимаем "Оформить заказ"')
    def make_burger(self, driver):
        self.click_on_constructor()
        self.add_bun(driver)
        self.add_ingredients(driver, 1)
        self.click_on_order_button()
        self.wait_order_number_change()
        order_number = self.get_order_number()
        self.click_on_cross()
        return order_number

