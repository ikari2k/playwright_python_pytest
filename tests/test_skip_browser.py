from playwright.sync_api._generated import Page
import pytest


# @pytest.mark.skip_browser("chromium")
@pytest.mark.only_browser("chromium")
def test_youtube(page: Page):
    page.goto("https://youtube.com")


# run with
# pytest tests/test_skip_browser.py --browser chromium --browser firefox
