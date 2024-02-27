from typing import Dict
import playwright
import pytest
from playwright.sync_api import BrowserType


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     iphone_11 = playwright.devices["iPhone 14 Pro"]
#     return {
#         **browser_context_args,
#         "ignore_https_errors": True,
#         "viewport": {
#             "width": 400,
#             "height": 400,
#         },
#         **iphone_11,
#     }


@pytest.fixture(scope="session")
def context(
    browser_type: BrowserType,
    browser_type_launch_args: Dict,
    browser_context_args: Dict,
):
    context = browser_type.launch_persistent_context(
        "./foobar",
        **{
            **browser_type_launch_args,
            **browser_context_args,
            "locale": "de-DE",
        }
    )
    yield context
    context.close()
