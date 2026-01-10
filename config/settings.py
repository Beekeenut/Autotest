
from dotenv import load_dotenv
import os


def get_base_url():
    load_dotenv()


    base_url = os.getenv("BASE_URL")
    if not base_url:
        base_url = "http://v2989688.hosted-by-vdsina.ru:8000/"


    if not base_url.startswith(("http://", "https://")):
        base_url = "http://" + base_url

    return base_url



