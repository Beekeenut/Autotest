from base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class RegistrPage(BasePage):

    REG_USERNAME_INPUT = ("xpath", "//*[@id='reg-username']")
    REG_PASSWORD_INPUT = ("xpath", "//*[@id='reg-password']")
    CREATE_BUTTON = ("xpath", "//button[@class='button' and @onclick='register()']")
    CAPTCHA_INPUT = ("xpath", "//*[@id='captcha']") 
    #REG_ERROR_MESSAGE = ("xpath", "//*[@id='notification' and contains(@class, 'error')]")
    REG_SUCCESS_INDICATOR = ("xpath", "//*[@id='notification' and contains(@class, 'success')]")

    def enter_reg_username(self, username):
        self.input_text(self.REG_USERNAME_INPUT, username)

    def enter_reg_password(self, password):
        self.input_text(self.REG_PASSWORD_INPUT, password)

    def enter_captcha(self, captcha):
        self.input_text(self.CAPTCHA_INPUT, captcha)

    def click_create(self):
        self.click_element(self.CREATE_BUTTON)



    def is_reg_succes(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.REG_SUCCESS_INDICATOR)
            )
            return True
        except TimeoutException:
            return False
        except Exception:
            return False