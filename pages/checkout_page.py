from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page:Page):
        self.page = page
        self.checkout_btn = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        self.success_msg = page.locator(".complete-header")

    def start_checkout(self):
        self.checkout_btn.click()
    def enter_details(self,fname,lname,zip_code):
        self.first_name.fill(fname)
        self.last_name.fill(lname)
        self.postal_code.fill(zip_code)
        self.continue_btn.click()

    def finish_checkout(self):
        self.finish_btn.click()
    def verify_success(self):
        expect(self.success_msg).to_have_text("Thank you for your order!")