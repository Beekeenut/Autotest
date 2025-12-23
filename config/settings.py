import random

#TODO это все функции функции хелперы, они никак не могут лежать в конфиге, надо вынести
def generate_word(length):
    word = ""
    for _ in range(length):
        char_code = random.randint(97, 122)
        word += chr(char_code)
    return word



#TODO BASE_URL вот это можно и нужно оставлять в конфиге, лучше тут сделать получение с env , если в env не передано, то используем это значение как дефолт (гугл в помощь по работе с енв)
BASE_URL = "http://v2989688.hosted-by-vdsina.ru:8000/"

#TODO вынести к тестам, определять до сьюта или во время теста, смотря как часто повторяется в коде
USERNAME = (generate_word(5))                             #(f"Test {random.randint(1, 5)}")
PASSWORD = (generate_word(5))                             #(f"Test {random.randint(1, 5)}")
#TODO вынести к тестам, определять до сьюта
CAPTCHA = "1234"


