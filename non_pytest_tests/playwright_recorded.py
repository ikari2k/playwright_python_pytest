from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    context.tracing.start(screenshots=True, sources=True, snapshots=True)
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("playwright")
    page.get_by_label("Search Wikipedia").press("Enter")
    page.get_by_text("Playwright", exact=True).click()
    page.get_by_role("link", name="Italian Renaissance").click()
    expect(page.locator("#firstHeading")).to_contain_text("Italian Renaissance")

    # ---------------------
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
