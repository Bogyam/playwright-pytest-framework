from playwright.sync_api import Page

class LoginPage(Page):

    def __init__(self, page: Page):
        self.page = page

        self.username=page.locator("#user-name")
        self.password=page.locator("#password")
        self.login_button = page.locator("#login-button")

    def load(self,url):
        self.page.goto(url)

    def login(self,user,pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()
