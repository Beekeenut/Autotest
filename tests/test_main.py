import pytest
from config.settings import USERNAME, PASSWORD, CAPTCHA


class TestLogin:

    def test_valid_registration(self, reg_page, login_page):
        """Тест успешной регистрацией"""
        login_page.click_registration()
        reg_page.enter_reg_username(USERNAME)
        reg_page.enter_reg_password(PASSWORD)
        reg_page.enter_captcha(CAPTCHA)
        reg_page.click_create()
        assert reg_page.is_reg_succes(), "Регистрация не выполнена"
    
    def test_invalid_password(self, login_page):
        """Тест с неверным паролем"""
        login_page.enter_username(USERNAME)
        login_page.enter_password("wrong_password")
        login_page.click_login()
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "Сообщение об ошибке не отображено"
        assert "Ошибка авторизации" in error_msg, "Некорректное сообщение об ошибке"

    def test_empty_username(self, login_page):
        """Тест с пустым именем пользователя"""
        login_page.enter_password(PASSWORD)
        login_page.click_login()
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "Сообщение об ошибке не отображено"
        assert "Ошибка авторизации" in error_msg, "Некорректное сообщение об ошибке"

    def test_valid_login(self, login_page):
        """Тест успешной авторизации с корректными данными"""
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login()
        assert login_page.is_logged_in(), "Вход не выполнен успешно"