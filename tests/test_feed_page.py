import allure

from locators.feed_page_locators import FeedPageLocators
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestFeedPage:

    @allure.title('При клике на заказ открывается всплывающее окно с деталями')
    def test_get_order_details(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_url(feed_page.feed_url)
        feed_page.click_on_last_order()

        assert 'Cостав' in feed_page.get_text_from_element(FeedPageLocators.ORDER_CONTAINS)

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders(self, driver, user, login):
        main_page = MainPage(driver)
        order_number = main_page.make_burger(driver)
        feed_page = FeedPage(driver)
        orders_done = feed_page.get_orders_done()

        assert order_number in orders_done

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_done_counter(self, driver, user, login):
        main_page = MainPage(driver)
        main_page.click_on_feed()
        feed_page = FeedPage(driver)
        orders = feed_page.get_orders_count()
        main_page.make_burger(driver)
        main_page.click_on_feed()

        assert FeedPage(driver).get_orders_count() == orders + 1

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_counter(self, driver, user, login):
        main_page = MainPage(driver)
        main_page.click_on_feed()
        feed_page = FeedPage(driver)
        today_orders = feed_page.get_today_orders_count()
        main_page.make_burger(driver)
        main_page.click_on_feed()

        assert FeedPage(driver).get_today_orders_count() == today_orders + 1

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_process(self, driver, user, login):
        main_page = MainPage(driver)
        order_number = main_page.make_burger(driver)
        feed_page = FeedPage(driver)

        assert order_number in feed_page.get_orders_in_process()

