import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators

@allure.title('Проверка переходов')
def test_navigation(driver):
    driver.get("https://stellarburgers.education-services.ru")
    main_page = MainPage(driver)

    with allure.step("Переход по клику на 'Лента заказов'"):
        main_page.click_button_order()
        order_page = OrderPage()
        assert order_page.is_all_time_counter_visible()

    with allure.step("Переход по клику на 'Конструктор'"):
        main_page.click_button_construct()
        assert driver.find_element(*MainPageLocators.BURGER_CONSTRUCT)