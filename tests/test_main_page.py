import allure

from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestMainPage:

    @allure.title('Переход по клику на «Конструктор»')
    def test_move_to_constructor(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_url(feed_page.feed_url)
        main_page = MainPage(driver)
        main_page.click_on_constructor()

        assert 'Соберите бургер' in main_page.get_text_from_element(MainPageLocators.BURGER_HEADER)

    @allure.title('Переход по клику на «Лента заказов»')
    def test_move_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.click_on_feed()
        feed_page = FeedPage(driver)

        assert 'Лента заказов' in feed_page.get_text_from_element(FeedPageLocators.FEED_HEADER)

    @allure.title('По клику на ингредиент появляется всплывающее окно с деталями')
    def test_get_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.click_on_ingredient()

        assert 'Детали ингредиента' in main_page.get_text_from_element(MainPageLocators.INGREDIENT_TEXT)

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.click_on_ingredient()
        main_page.click_on_cross()

        assert 'Соберите бургер' in main_page.get_text_from_element(MainPageLocators.BURGER_HEADER)

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredients_count(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.add_ingredients(driver, 2)

        assert main_page.get_ingredients_count() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order(self, driver, user, login):
        main_page = MainPage(driver)
        main_page.add_bun(driver)
        main_page.add_ingredients(driver, 3)
        main_page.click_on_order_button()

        assert 'Соберите бургер' in main_page.get_text_from_element(MainPageLocators.BURGER_HEADER)

