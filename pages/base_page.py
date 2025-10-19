from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    

    @allure.step('Подождать загрузки элемента')
    def wait_visibility_of_element(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator))
    

    @allure.step('Клик по элементу')
    def click_on_element(self, *locator):
        self.driver.find_element(*locator).click()


    @allure.step('Поиск элемента')
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Получение текста элемента')
    def get_element_text(self, *locator):
        return self.wait_for_element(*locator).text