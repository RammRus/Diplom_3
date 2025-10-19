from selenium.webdriver.common.by import By

class OrderPageLocators:
    COUNTER_ALL_TIME = (By.CLASS_NAME, 'undefined mb-15') #Счетчик заказов за все время
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']") #Счетчик заказов за сегодня
    AT_WORK = (By.CLASS_NAME, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi') #Раздел "В работе"