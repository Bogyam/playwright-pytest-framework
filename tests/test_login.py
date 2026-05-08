from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD,INVALID_USER,INVALID_PASS
from playwright.sync_api import expect

def test_valid_login(page):
    login = LoginPage(page)

    login.load(BASE_URL)
    login.login(USERNAME, PASSWORD)

def test_invalid_login(page):
    login = LoginPage(page)
    login.load(BASE_URL)
    login.login(INVALID_USER, INVALID_PASS)



