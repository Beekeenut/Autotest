from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    #TODO поправил описание, пишем просто что делает метод, не пишем что служит поиском в других методах, а если другие методы уберут?
    def find_element(self, locator):
        """
        Поиск элемента по локатору
        :param locator: локатор
        :return: возвращает найденный в DOM элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """
        Клик по элементу
        :param locator: локатор
        :return:
        """
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        """
        Вставка текста
        :param locator: локатор
               text: - текст для вставки
        :return:
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

