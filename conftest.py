import random
import string
import pytest
from pages.login_page import LoginPage
from pages.reg_page import RegistrPage
from selenium import webdriver
from config.settings import get_base_url #, LOGIN_PATH

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # для безголового режима
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    driver.get(get_base_url())
    return LoginPage(driver)

@pytest.fixture
def reg_page(driver):
    driver.get(get_base_url())
    return RegistrPage(driver)



@pytest.fixture
def credentials():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    password = ''.join(random.choices(
        string.ascii_letters + string.digits,
        k=12
    ))
    return {"username": username, "password": password}