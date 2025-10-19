from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step("Проверка отображения счетчика 'Всё время'")
    def is_all_time_counter_visible(self):
        return self.wait_visibility_of_element(OrderPageLocators.COUNTER_ALL_TIME)

    @allure.step("Проверка отображения счетчика 'За сегодня'")
    def is_today_counter_visible(self):
        return self.wait_visibility_of_element(OrderPageLocators.COUNTER_TODAY)

    @allure.step("Проверка раздела 'В работе'")
    def is_in_progress_section_visible(self):
        return self.wait_visibility_of_element(OrderPageLocators.AT_WORK)

    @allure.step("Получить число заказов за всё время")
    def get_all_time_order_count(self):
        elem = self.find_element(OrderPageLocators.COUNTER_ALL_TIME)
        return int(elem.text)

    @allure.step("Получить число заказов за сегодня")
    def get_today_order_count(self):
        elem = self.find_element(OrderPageLocators.COUNTER_TODAY)
        return int(elem.text)
    
    @allure.step("Получить заказ из раздела 'В работе'")
    def get_order_in_work(self):
        order = OrderPageLocators.AT_WORK
        return self.wait_visibility_of_element(order)