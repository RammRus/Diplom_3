from selenium.webdriver.common.by import By

class AuthPageLocators:
    EMAIL = (By.XPATH, "//input[@placeholder='Email']") #Поле Email
    PASSWORD = (By.XPATH, "//input[@placeholder='Пароль']") #Поле Пароль
    BUTTON_LOGIN = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains (@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa') and text()='Войти']") #Кнопка Войти