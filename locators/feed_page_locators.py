from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_HEADER = By.XPATH, './/h1[text()="Лента заказов"]'
    ORDER_PANEL = By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]'
    ORDERS = By.XPATH, './/div[2]/p[contains(@class,"OrderFeed_number__2MbrQ")]'
    LAST_ORDER = By.XPATH, './/div[contains(@class,"OrderHistory_dataBox__1mkxK")]'
    ORDER_CONTAINS = By.XPATH, './/div/p[3][text()="Cостав"]'
    ORDERS_TODAY = By.XPATH, './/div[3]/p[contains(@class,"OrderFeed_number__2MbrQ")]'
    ORDERS_IN_PROCESS = By.XPATH, './/ul[2]/li[contains(@class,"text text_type_digits-default")]'
    ORDERS_DONE = By.XPATH, './/ul[1][contains(@class,"OrderFeed_orderList")]'
