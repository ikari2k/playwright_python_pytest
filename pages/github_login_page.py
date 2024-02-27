class GithubLoginPage:
    def __init__(self, page) -> None:
        self.page = page

    def enter_username(self, username: str | None):
        self.page.click('input[id="login_field"]')
        self.page.fill('input[id="login_field"]', username)

    def enter_password(self, password: str | None):
        self.page.fill('input[id="password"]', password)

    def click_login_button(self):
        self.page.get_by_role("button", name="Sign in", exact=True).click()
