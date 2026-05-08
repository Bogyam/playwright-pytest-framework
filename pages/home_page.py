from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.product_names = page.locator(".inventory_item_name")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_product_by_name(self, product_name):

        count = self.product_names.count()

        for i in range(count):
            name = self.product_names.nth(i).inner_text()

            if name == product_name:
                item = self.product_names.nth(i).locator("xpath=ancestor::div[@class='inventory_item']")
                item.locator("button").click()
                break

    def open_cart(self):
        self.cart_icon.click()