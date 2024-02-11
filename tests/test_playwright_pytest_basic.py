from playwright.sync_api import Page


def test_visit_youtube(page: Page, browser_type):
    browser_type.launch(headless=True, slow_mo=2000)
    page.goto("https://youtube.com")
