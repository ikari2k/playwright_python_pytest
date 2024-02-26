from playwright.sync_api import Page, expect


def test_example(page: Page, browser_type, context) -> None:
    browser_type.launch(headless=True, slow_mo=2000)
    context.tracing.start(screenshots=True, sources=True, snapshots=True)
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("trump")
    page.get_by_role("link", name="Trump Tower Skyscraper in").click()
    expect(
        page.get_by_role("heading", name="Trump Tower").locator("span")
    ).to_be_visible()
    context.tracing.stop(path="trace.zip")
