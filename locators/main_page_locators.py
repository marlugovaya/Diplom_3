from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'
    ACCOUNT_BUTTON = By.XPATH, './/p[text()="Личный Кабинет"]'
    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text()="Конструктор"]'
    FEED_BUTTON = By.XPATH, './/p[text()="Лента Заказов"]'
    BURGER_HEADER = By.XPATH, './/h1[text()="Соберите бургер"]'
    INGREDIENT = By.XPATH, './/ul[3]/a[1]/img[contains(@class,"BurgerIngredient_ingredient")]'
    INGREDIENT_TEXT = By.XPATH, './/div/h2[text()="Детали ингредиента"]'
    INGREDIENT_COUNT = By.XPATH, './/ul[3]/a[1]/div[1]/p[contains(@class,"counter_counter")]'
    INGREDIENT_DETAILS = By.XPATH, './/h2[text()="Детали ингредиента"]'
    BUN = By.XPATH, './/ul[1]/a[1]/img[contains(@class,"BurgerIngredient_ingredient")]'
    CROSS_BUTTON = By.XPATH, './/button[@type="button"]'
    CONSTRUCTOR_BASKET = By.XPATH, './/ul[contains(@class,"BurgerConstructor_basket")]'

    ORDER_MESSAGE = By.XPATH, '//div[contains(@class,"Modal_modal__contentBox__sCy8X")]'
    ORDER_NUMBER = By.XPATH, '//div/h2[contains(@class,"Modal_modal__title_shadow")]'
    DEFAULT_ORDER_NUMBER = By.XPATH, '//div/h2[text()="9999"]'

