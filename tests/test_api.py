import os
from typing import Generator
from dotenv import load_dotenv
from playwright.sync_api import Playwright, Page, APIRequestContext, expect
import pytest

load_dotenv()
GITHUB_API_TOKEN = os.environ.get("GITHUB_API_TOKEN")
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN no set"

GITHUB_USER = os.environ.get("GITHUB_USER")
assert GITHUB_USER, "GITHUB_USER not set"

GITHUB_REPO = os.environ.get("GITHUB_REPO")


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_API_TOKEN}",
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )
    print("Request Context Created")
    yield request_context
    request_context.dispose()
    print("Request Context Removed")


@pytest.fixture(scope="session", autouse=True)
def create_test_repo(
    api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    new_repo = api_request_context.post("/user/repos", data={"name": GITHUB_REPO})
    assert new_repo.ok
    print(f"{GITHUB_REPO} Repo Created")
    yield

    delete_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
    assert delete_repo.ok
    print(f"{GITHUB_REPO} Repo Deleted")


def test_bug_report(api_request_context: APIRequestContext) -> None:
    data = {"title": "[Bug] report 1", "body": "Bug description"}
    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
    )
    assert new_issue.ok

    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok

    issues_response = issues.json()
    issue = list(
        filter(lambda issue: issue["title"] == "[Bug] report 1", issues_response)
    )[0]
    assert issue
    assert issue["body"] == "Bug description"


def test_feature(api_request_context: APIRequestContext) -> None:
    data = {"title": "[Feature] request 1", "body": "Feature description"}

    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
    )

    assert new_issue.ok

    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok

    issues_response = issues.json()
    issue = list(
        filter(lambda issue: issue["title"] == "[Feature] request 1", issues_response)
    )[0]
    assert issue
    assert issue["body"] == "Feature description"
