from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import BASE_URL, USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ZIP_CODE

def test_complete_checkout_flow(page):

    product = "Sauce Labs Backpack"

    # login
    login = LoginPage(page)
    login.load(BASE_URL)
    login.login(USERNAME, PASSWORD)

    # add product
    home = HomePage(page)
    home.add_product_by_name(product)
    home.open_cart()

    # cart
    cart = CartPage(page)
    cart.verify_product_in_cart(product)

    # checkout
    checkout = CheckoutPage(page)
    checkout.start_checkout()
    checkout.enter_details(FIRST_NAME, LAST_NAME, ZIP_CODE)
    checkout.finish_checkout()

    # validation
    checkout.verify_success()