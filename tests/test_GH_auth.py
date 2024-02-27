import os
from playwright.sync_api import expect


def test_auth(page):
    page.goto("https://github.com/login")
    page.locator('input[id="login_field"]').click
    page.locator('input[id="login_field"]').fill(os.environ.get("GITHUB_USER_EMAIL"))
    page.locator('input[id="password"]').click
    page.locator('input[id="password"]').fill(os.environ.get("GITHUB_USER_PASS")
    page.get_by_role("button", name="Sign in", exact=True).click()
    page.wait_for_url("https://github.com/")
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
