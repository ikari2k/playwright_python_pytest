from playwright.sync_api import Page, expect


def test_example(page: Page, browser, browser_type) -> None:
    browser_type.launch(headless=True, slow_mo=2000)
    browser.start_tracing(path="trace.json", screenshots=True)
    page.goto("https://www.wikipedia.org/")
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("trump")
    page.get_by_role("link", name="Trump Tower Skyscraper in").click()
    expect(
        page.get_by_role("heading", name="Trump Tower").locator("span")
    ).to_be_visible()
    browser.stop_tracing()
