from base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class LoginPage(BasePage):

    USERNAME_INPUT = ("xpath", "//*[@id='username']")
    PASSWORD_INPUT = ("xpath", "//*[@id='password']")
    LOGIN_BUTTON = ("xpath", "//*[@id='login-card']/div/button[1]")
    REGISTRATION_BUTTON = ("xpath", "//*[@id='login-card']/div/button[2]") 
    ERROR_MESSAGE = ("xpath", "//*[@id='notification' and contains(@class, 'error')]")
    SUCCESS_INDICATOR = ("xpath", "//*[@id='notification' and contains(@class, 'success')]")

    def enter_username(self, username):
        self.input_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def click_registration(self):
        self.click_element(self.REGISTRATION_BUTTON)

    def get_error_message(self, timeout=5):
        try:
            error_element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error_element.text
        except (TimeoutException, NoSuchElementException):
            return None
    
    def is_logged_in(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.SUCCESS_INDICATOR)
            )
            return True
        except TimeoutException:
            return False
        except Exception:
            return False