import pytest
from pages.login_page import LoginPage
from pages.reg_page import RegistrPage
from selenium import webdriver
from config.settings import BASE_URL #, LOGIN_PATH

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
    driver.get(f"{BASE_URL}") #{LOGIN_PATH}
    return LoginPage(driver)

@pytest.fixture
def reg_page(driver):
    driver.get(f"{BASE_URL}") #{LOGIN_PATH}
    return RegistrPage(driver)
