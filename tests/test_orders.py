import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from locators.auth_page_locators import AuthPageLocators
from pages.auth_page import AuthPage
from pages.order_page import OrderPage
from pages.main_page import MainPage

@allure.title('Проверка счетчиков на странице "Лента заказов"')
def test_orders_count(driver):
    order_page = OrderPage(driver)
    auth_page = AuthPage(driver)
    main_page = MainPage(driver)
    initial_total = order_page.get_all_time_order_count()
    initial_today = order_page.get_today_order_count()
    with allure.step('Проходим авторизацию'):
        main_page.click_button_auth()
        auth_page.enter_email('ramm@test.ru')
        auth_page.enter_password('123456')
        auth_page.click_login()
    with allure.step('Создаем заказ'):
        main_page.click_button_construct()
        main_page.drag_ingredient_in_constructor()
        main_page.drag_bun_in_constructor()
        main_page.click_on_button_order()
    with allure.step('Переход на страницу "Лента заказов"'):
        main_page.click_button_order()
    with allure.step('Проверка счетчиков'):
        new_total = order_page.get_all_time_order_count()
        new_today = order_page.get_today_order_count()
        assert new_total == initial_total + 1
        assert new_today == initial_today + 1
