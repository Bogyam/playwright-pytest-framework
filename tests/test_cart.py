from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from utils.config import BASE_URL, USERNAME, PASSWORD

def test_add_specific_product(page):

    product = "Sauce Labs Backpack"

    # login
    login = LoginPage(page)
    login.load(BASE_URL)
    login.login(USERNAME, PASSWORD)

    # home page
    home = HomePage(page)
    home.add_product_by_name(product)
    home.open_cart()

    # cart validation
    cart = CartPage(page)
    cart.verify_product_in_cart(product)


def test_remove_product(page):

    product = "Sauce Labs Backpack"

    login = LoginPage(page)
    login.load(BASE_URL)
    login.login(USERNAME, PASSWORD)

    home = HomePage(page)
    home.add_product_by_name(product)
    home.open_cart()

    cart = CartPage(page)
    cart.remove_product()
    cart.verify_cart_empty()