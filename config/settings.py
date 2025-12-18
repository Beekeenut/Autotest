import random

def generate_word(length):
    word = ""
    for _ in range(length):
        char_code = random.randint(97, 122)
        word += chr(char_code)
    return word




BASE_URL = "http://v2989688.hosted-by-vdsina.ru:8000/"

USERNAME = (generate_word(5))                             #(f"Test {random.randint(1, 5)}")
PASSWORD = (generate_word(5))                             #(f"Test {random.randint(1, 5)}")
CAPTCHA = "1234"


