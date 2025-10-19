import pytest
import allure
from pages.main_page import MainPage

@allure.title('Работа с ингредиентами')
class TestIngredient:
    def test_ingredient_information(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        main_page = MainPage(driver)

        with allure.step('Проверка, что при клике на ингредиент, всплывает окно с информацией об ингредиенте'):
            main_page.open_bun_details()
            title = main_page.get_element_text()
            assert title


    def test_closed_inform_about_ingredient(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        main_page = MainPage(driver)
        main_page.open_bun_details()
        with allure.step('Проверка, что окно с информацией об ингредиенте закрывается при нажатии на крестик'):
            main_page.open_bun_details()
            main_page.close_bun_details()
            assert main_page.burger_construct()


    def test_counter_value(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        main_page = MainPage(driver)
        with allure.step('Проверка изменения счетчика ингредиента, после добавления его в заказ'):
            main_page.drag_ingredient_in_constructor()
            assert main_page.get_counter_value() == 1