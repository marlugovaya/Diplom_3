from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_HEADER = By.XPATH, './/h1[text()="Лента заказов"]'
    ORDER_PANEL = By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]'
    ORDERS = By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class, "OrderFeed_number")]'
    LAST_ORDER = By.XPATH, './/div[contains(@class,"OrderHistory_dataBox__1mkxK")]'
    ORDER_CONTAINS = By.XPATH, './/section[contains(@class, "opened__3ISw4")]'
    ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class, "OrderFeed_number")]'
    ORDERS_IN_PROCESS = By.XPATH, './/ul[contains(@class,"OrderFeed")]/li[contains(@class,"text")]'
    ORDERS_DONE = By.XPATH, './/li[contains(@class, "text text_type_digits-default mb-2")]'
