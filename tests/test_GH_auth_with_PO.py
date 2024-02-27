import os
from playwright.sync_api import expect, Page

from pages.github_login_page import GithubLoginPage


def test_auth(page):
    page.goto("https://github.com/login")
    github_login_page = GithubLoginPage(page)
    github_login_page.enter_username(os.environ.get("GITHUB_USER_EMAIL"))
    github_login_page.enter_password(os.environ.get("GITHUB_USER_PASS"))
    github_login_page.click_login_button()
    page.wait_for_url("https://github.com/")
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()


def test_auth_with_fixture(page: Page, github_login_page: GithubLoginPage):
    page.goto("https://github.com/login")
    github_login_page.enter_username(os.environ.get("GITHUB_USER_EMAIL"))
    github_login_page.enter_password(os.environ.get("GITHUB_USER_PASS"))
    github_login_page.click_login_button()
    page.wait_for_url("https://github.com/")
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
