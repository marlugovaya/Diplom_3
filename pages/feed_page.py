import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    feed_url = 'https://stellarburgers.nomoreparties.site/feed'

    @allure.step('Получаем количество заказов')
    def get_orders_count(self):
        self.open_url(self.feed_url)
        return int(self.get_text_from_element(FeedPageLocators.ORDERS))

    @allure.step('Кликаем на последний заказ')
    def click_on_last_order(self):
        self.click_on_element(FeedPageLocators.LAST_ORDER)

    @allure.step('Получаем количество сегодняшних заказов')
    def get_today_orders_count(self):
        self.open_url(self.feed_url)
        return int(self.get_text_from_element(FeedPageLocators.ORDERS_TODAY))

    @allure.step('Получаем заказы, которые готовы')
    def get_orders_done(self):
        self.open_url(self.feed_url)
        return str(self.get_text_from_element(FeedPageLocators.ORDERS_DONE))

    @allure.step('Получаем заказы, которые в работе')
    def get_orders_in_process(self):
        self.open_url(self.feed_url)
        return str(self.get_text_from_element(FeedPageLocators.ORDERS_IN_PROCESS))