def test_download(page):
    page.goto("https://www.jetbrains.com/pycharm/download/#section=windows")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download").nth(1).click()
    download = download_info.value
    print(download.path)
    download.save_as(
        "/Users/mateuszpluta/Projects/playwright_python_pytest/tests/down.txt"
    )
