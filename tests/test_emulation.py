import playwright
from playwright.sync_api import sync_playwright, Playwright
import pytest


# @pytest.fixture(
#     params=[
#         {
#             "viewport": {"width": 414, "height": 896},
#             "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
#         },
#         {
#             "viewport": {"width": 768, "height": 1024},
#             "user_agent": "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/85.0.4183.109 Mobile/15E148 Safari/604.1",
#             "device_scale_factor": 2,
#         },
#     ]
# )
# def options(request):
#     print(request.param)
#     return request.param


def test_device_emulation(browser):
    with browser.new_context() as context:
        page = context.new_page()
        page.goto("https://example.com")
        assert "Example" in page.title()
