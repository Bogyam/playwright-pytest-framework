from playwright.sync_api import Page, expect

class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator(".inventory_item_name")
        self.remove_buttons = page.locator("button[data-test^='remove']")

    def verify_product_in_cart(self, product_name):
        expect(self.cart_items).to_contain_text([product_name])

    def remove_product(self):
        self.remove_buttons.first.click()

    def verify_cart_empty(self):
        expect(self.cart_items).to_have_count(0)