from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_CONSTRUCT = (By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2") #Кнопка Конструктор
    BUTTON_ORDER_FEED = (By.CLASS_NAME, "AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo") #Кнопка Лента заказов
    BUN = (By.XPATH, "//div[text()='Флюоресцентная булка R2-D3']") #Булка
    SAUCE = (By.XPATH, "/ul/div[contains(@class, 'BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4') and text('Соус Spicy-X')]")
    ING_DETAILS = (By.XPATH, "//div[text()='Детали ингредиента']") #Окно деталей ингредиента
    BUTTON_CLOSED = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK") #Крестик, закрывающий окно деталей ингредиента
    BURGER_CONSTRUCT = (By.CLASS_NAME, "BurgerConstructor_basket__29Cd7 mt-25 ") #Раздел с созданием бургера(его компоненты)
    SAUCE_COUNTER = (By.XPATH, "//a[contains(@class, 'counter_counter__ZNLkj') and contains(@class, 'counter_default__28sqi')]/div[contains(@class, 'counter_counter__ZNLkj') and contains(@class, 'counter_default__28sqi')]") #Счетчик Соуса Spicy-X
    AUTH_BUTTON = (By.XPATH, "//a[text()='Личный кабинет']") #Кнопка Личный кабинет
    MAIN_HEADER = (By.XPATH, "/main[@class, 'App_componentContainer__2JC2W']") #Кнопка "Stellar Burger", которая ведет на главную страницу "Конструктор"
    BUTTON_CREATE_ORDER = (By.XPATH, "//div[text()='Оформить заказ']") #Кнопка "Оформить заказ"
    NUMBER_ORDER = (By.CLASS_NAME, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')