import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.title('Проверка переходов')
class TestNavigation:
    def test_navigation_order(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        main_page = MainPage(driver)

        with allure.step("Переход по клику на 'Лента заказов'"):
            main_page.click_button_order()
            order_page = OrderPage()
            assert order_page.is_all_time_counter_visible()

    def test_navigation_construct(driver):
        driver.get("https://stellarburgers.education-services.ru/feed")
        main_page = MainPage(driver)
        with allure.step("Переход по клику на 'Конструктор'"):
            main_page.click_button_construct()
            assert main_page.burger_construct()