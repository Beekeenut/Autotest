
from dotenv import load_dotenv
import os


#TODO BASE_URL вот это можно и нужно оставлять в конфиге, лучше тут сделать получение с env , если в env не передано, то используем это значение как дефолт (гугл в помощь по работе с енв)
def get_base_url():
    load_dotenv()


    base_url = os.getenv("BASE_URL")
    if not base_url:
        base_url = "http://v2989688.hosted-by-vdsina.ru:8000/"


    if not base_url.startswith(("http://", "https://")):
        base_url = "http://" + base_url

    return base_url



#BASE_URL = "http://v2989688.hosted-by-vdsina.ru:8000/"

#TODO вынести к тестам, определять до сьюта или во время теста, смотря как часто повторяется в коде

#TODO вынести к тестам, определять до сьюта



