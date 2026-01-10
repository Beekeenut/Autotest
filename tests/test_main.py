import random

#TODO на будущее, обычно таких функций хелперов очень много и они нужны для разных модулей. Их выносят в отдельные папки с разной функциональностью, все держать в файле с тестами очень плохая практика.
# Тут можно, так как вспомогательный метод всего один
def generate_word(length):
    word = ""
    for _ in range(length):
        char_code = random.randint(97, 122)
        word += chr(char_code)
    return word
#TODO не нужно делать отдельный класс, вставить в класс с тестами
class TestVar:
        USERNAME = (generate_word(5))
        PASSWORD = (generate_word(5))
        CAPTCHA = "1234"

class TestLogin:
   # прям сюда

    def test_valid_registration(self, reg_page, login_page):
        """Тест успешной регистрацией"""
        login_page.click_registration()
        reg_page.enter_reg_username(TestVar.USERNAME)
        reg_page.enter_reg_password(TestVar.PASSWORD)
        reg_page.enter_captcha(TestVar.CAPTCHA)
        reg_page.click_create()
        assert reg_page.is_reg_succes(), "Регистрация не выполнена"
    
    def test_invalid_password(self, login_page):
        """Тест с неверным паролем"""
        login_page.enter_username(TestVar.USERNAME)
        login_page.enter_password("wrong_password")
        login_page.click_login()
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "Сообщение об ошибке не отображено"
        assert "Ошибка авторизации" in error_msg, "Некорректное сообщение об ошибке"

    def test_empty_username(self, login_page):
        """Тест с пустым именем пользователя"""
        login_page.enter_password(TestVar.PASSWORD)
        login_page.click_login()
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "Сообщение об ошибке не отображено"
        assert "Ошибка авторизации" in error_msg, "Некорректное сообщение об ошибке"

    def test_valid_login(self, login_page, reg_page, credentials):
        """Тест успешной авторизации с корректными данными"""
        USERNAME = credentials["username"]   # Добавил фикстуру, чтобы генерились новые ТД, а не брались старые. С фикстурами еще надо разбираться, не до конца понимаю
        PASSWORD = credentials["password"]

        login_page.click_registration()
        reg_page.enter_reg_username(USERNAME)
        reg_page.enter_reg_password(PASSWORD)
        reg_page.enter_captcha(TestVar.CAPTCHA)
        reg_page.click_create()
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login()
        assert login_page.is_logged_in(), "Вход не выполнен успешно"