from .base_page import BasePage
from locators.auth_page_locators import AuthPageLocators
import allure

class AuthPage(BasePage):

    @allure.step("Ввод email")
    def enter_email(self, email):
        input_email = self.find_element(AuthPageLocators.EMAIL)
        input_email.clear()
        input_email.send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        input_pass = self.find_element(AuthPageLocators.PASSWORD)
        input_pass.clear()
        input_pass.send_keys(password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login(self):
        self.click_element(AuthPageLocators.BUTTON_LOGIN)