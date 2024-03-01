![playwright workflow](https://github.com/ikari2k/playwright_python_pytest/actions/workflows/playwright.yml/badge.svg)

Latest Test Report via Allure can be found --> https://ikari2k.github.io/playwright_python_pytest/

# What is this repo about:
This is my scratchpad for all things related to pytest and playwright.


# Notes

### Advantages of Async Playwright:

**Asynchronous Execution:** Async Playwright is designed to work asynchronously, meaning it can perform multiple tasks concurrently without blocking the main thread. This can lead to better performance and scalability, particularly in applications where there are many browser operations or where responsiveness is critical.

**Suitable for IO-bound Tasks:** If your automation tasks involve a lot of waiting for network requests, file operations, or other IO-bound operations, async programming can be more efficient. It allows the program to continue executing other tasks while waiting for IO operations to complete.

**Modern Python Development:** Asynchronous programming has become increasingly popular in modern Python development, especially with the advent of async/await syntax in Python 3.5+. Async Playwright fits well into this ecosystem and can be seamlessly integrated with other async libraries.

**Event Loop Control:** Async Playwright provides more control over the event loop, which can be beneficial in certain scenarios where you need fine-grained control over concurrency and execution flow.

### Advantages of Sync Playwright:

**Simplicity and Familiarity:** Sync Playwright follows a synchronous execution model, which may be more intuitive and easier to understand for developers who are not familiar with asynchronous programming concepts. If you're more comfortable with synchronous programming or if your project doesn't benefit significantly from asynchronous execution, Sync Playwright might be a better fit.

**Compatibility with Sync Codebases:** If you're integrating Playwright into an existing codebase that is primarily synchronous, using Sync Playwright can simplify the integration process and avoid the need to refactor large portions of your code.

**Blocking Calls:** In certain scenarios, particularly when dealing with CPU-bound tasks or when simplicity is prioritized over concurrency, synchronous execution might be sufficient and easier to reason about.

**Debugging:** Debugging synchronous code can be more straightforward compared to debugging asynchronous code, especially for developers who are not yet comfortable with asynchronous programming paradigms.

In summary, the choice between Async Playwright and Sync Playwright depends on factors such as your familiarity with asynchronous programming, the nature of your automation tasks, performance requirements, and compatibility with existing codebases. Both libraries have their strengths, and the decision should be based on what best fits the needs of your project.

### Auto-waiting

Playwright performs a range of actionability checks on the elements
before making actions to ensure these actions behave as expected.
It auto-waits for all the relevant checks to pass and only then
performs the requested action.
For example, for page.click(selector, **kwargs), Playwright will
ensure that:
-  element is Attached to the DOM
-  element is Visible
- element is Stable, as in not animating or completed animation
- element Receives Events, as in not obscured by other
elements
- element is Enabled

### Forcing actions

Some actions like page.click(selector, **kwargs) support force option that disables
non-essential actionability checks, for example passing truthy force to
peal reeves cir events) method will not check that the target element