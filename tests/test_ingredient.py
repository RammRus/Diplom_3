import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage

@allure.title('Работа с ингредиентами')
def test_ingredient(driver):
    driver.get("https://stellarburgers.education-services.ru")
    main_page = MainPage(driver)

    with allure.step('Проверка, что при клике на ингредиент, всплывает окно с информацией об ингредиенте'):
        main_page.open_bun_details()
        assert driver.find_element(*MainPageLocators.ING_DETAILS)

    with allure.step('Проверка, что окно с информацией об ингредиенте закрывается при нажатии на крестик'):
        main_page.open_bun_details()
        main_page.click_on_element(*MainPageLocators.BUTTON_CLOSED)
        assert driver.current_url == 'https://stellarburgers.education-services.ru/'

    with allure.step('Проверка изменения счетчика ингредиента, после добавления его в заказ'):
        main_page.drag_ingredient_in_constructor()
        assert main_page.get_counter_value() == 1