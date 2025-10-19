from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure
from selenium.webdriver import ActionChains

class MainPage(BasePage):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Ожидание прогрузки главной страницы')
    def is_main_header_visible(self):
        return self.wait_visibility_of_element(MainPageLocators.MAIN_HEADER)
    
    @allure.step('Клик по кнопке "Конструктор"')
    def click_button_construct(self):
        but_con = self.wait_clickable_of_element(MainPageLocators.BUTTON_CONSTRUCT)
        but_con.click()

    @allure.step('Клик по кнопку "Лента заказов"')
    def click_button_order(self):
        but_ord = self.wait_clickable_of_element(MainPageLocators.BUTTON_CONSTRUCT)
        but_ord.click()

    @allure.step("Клик по ингредиенту")
    def open_bun_details(self):
        self.click_on_element(MainPageLocators.BUN)

    @allure.step('Получение заголовка окна с информацией об ингредиенте')
    def get_information_ingredient(self):
        self.get_element_text(MainPageLocators.ING_DETAILS)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_button_auth(self):
        self.click_on_element(MainPageLocators.AUTH_BUTTON)

    @allure.step("Закрытие окна информации об ингредиенте кликом по крестику")
    def close_bun_details(self):
        self.click_on_element(MainPageLocators.BUTTON_CLOSED)

    @allure.step('Показание значения счетчика для ингредиента')
    def get_counter_value(self):
        counter = self.find_element(MainPageLocators.SAUCE_COUNTER)
        return int(counter.text)
    
    @allure.step('Перенос ингредиента в коструктор')
    def drag_ingredient_in_constructor(self):
        source = self.find_element(MainPageLocators.SAUCE)
        target = self.find_element(MainPageLocators.BURGER_CONSTRUCT)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step('Перенос булки в конструктор')
    def drag_bun_in_constructor(self):
        source = self.find_element(MainPageLocators.BUN)
        targer = self.find_element(MainPageLocators.BURGER_CONSTRUCT)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, targer).perform()

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_button_order(self):
        self.click_on_element(MainPageLocators.BUTTON_CREATE_ORDER)

    @allure.step('Раздел со сбором бургера')
    def burger_construct(self):
        self.find_element(MainPageLocators.BURGER_CONSTRUCT)

    @allure.step("Получить номер заказа")
    def get_number_order(self):
        self.drag_bun_in_constructor()
        self.click_on_button_order()
        number = self.find_element(MainPageLocators.NUMBER_ORDER)
        return int(number.text)

