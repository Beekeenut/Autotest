from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    #TODO добавить описания методов и входные/выходные параметры
    def find_element(self, locator):
        """
        Метод нужен для поиска элемента в методах click и input по заданному локатору(тип пути локатора, путь)
        :param locator: входной параметр,
        :return: возвращает найденный в DOM элемент (выходной параметр)
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """
        Метод нужен для клика по найденному элементу
        :param locator: входной параметр - для поиска по локатору,
        :return: возвращает none?  (выходной параметр)
        """
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        """
        Метод нужен для вставки текста
        :param locator: входной параметр - для поиска по локатору, text: - текст, который будет вставлен в поле методом send_keys
        :return: возвращает none?  (выходной параметр)
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

