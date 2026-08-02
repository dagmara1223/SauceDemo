### 1. Chronological record of prompt logs

A chronological record of the AI-assisted workflows using **Claude**, conversational mode. This section covers: what was asked, the response
and how the response was corrected. The prompts below are paraphrased from the actual conversation.

## Step 0️⃣ - initialization
**Prompt**: "Hello, I am facing the task where I should create AI-automated tests and maximize the quality of the result. I am explicitly asking for
strategy, not an implementation. Which three tests would You recommend to use on a mini-Internet shop site with login, items that we could add to cart,
finalized payments? We also have a hamburger left-slide as a feature, we can sort the products by the Name or Price, and we are provided with a list of accepted
usernames to LogIn and usernames that were blocked / excluded." <br>
**Response**: AI Agent pointed out that we should focus on the mentioned: 1. login trap, 2. create full flow: logging -> adding items (preferably 2+) -> cart -> summary
-> payment / acceptance and 3. hamburger slide. <br>
**My Decision**: I accepted two provided examples: 1. and 2. but decided to go with a product sorting check as 3. and describe the lack of Slide Menu tests in **approach.md**. (link)

## Step 1️⃣ - first page
**Prompt**: "I have created the BasePage class from which all page objects inherit. I also
created our first Login page + tests. Please suggest a maintainable project infrastructure for a Playwright + Pytest framework, including conftest.py, reusable fixtures, authentication handling, CI and project documentation. Focus on architecture rather than implementation" <br>
**Response**: AI Agent proposed a project structure similar to my initial design, including reusable pytest fixtures, centralized configuration (pytest.ini), a dedicated conftest.py and project documentation. It also suggested a more advanced authentication mechanism based on Playwright's storage_state, where the user logs in once per session and the saved session is reused by the remaining tests. <br>
**My Decision**: I accepted the response and decided to add GitHub Actions. However, I have
also decided not to proceed with the storage_state idea since this specific task requires only
three tests - performing a fresh login in each relevant test costs little execution time, while storage_state would make the code noticeably more complex.

## Step 2️⃣ - debugging: locators
**Prompt**: "The tests fail even though the elements are visible in the browser and Playwright reports that the locator cannot find the element. Help me identify whether the issue is related to the locator strategy, the application itself or the Playwright configuration. Explain the reasoning and where to look for the bug." <br>
**Response**: AI suggested verifying whether the application used Playwright's default data-testid attribute or a custom attribute - SauceDemo exposes testing hooks as data-test, while get_by_test_id() expects data-testid unless configured otherwise. <br>
**My Decision**: AI was right, and the bug came from the code the model had generated earlier. I fixed it globally with a single session-scoped fixture instead of rewriting every locator:
playwright.selectors.set_test_id_attribute("data-test") <br>

## Step 3️⃣ - debugging: naming
**Prompt**: "Test login negative still fails after fixing the locators. Help me identify the root cause - why is it failing? Explain what should be verified first and whether the problem seems to be correlated to a bug in the test or rather in the login page."
**Response**: AI Agent suggested a path that helped me with the debugging. It identified several possible causes, including incorrect page locators, project import structure, inconsistent naming introduced during refactoring (URL vs url) and finally incorrect expected assertion values.
**My Decision/Resolution**: The issue was, in fact, correlated to misspelling "url" and using
"URL" everywhere, plus a mismatch between the method names I had renamed in LoginPage and the names still called in the test. After that - all 3 passed.

## Step 4️⃣ - when work was done
**Prompt**: "Please review my current logic and implementation. The tests are working fine,
all 3 of them: e2e, data and negative (test for login). Focus on InventoryPage, CartPage and CheckoutPage - on maintainability, spelling, fluent usage, correct variable names, and whether the public API of each page is coherent. Please don't change the code, just give me some finishing touches tips" <br>
**Response**: Several improvements were suggested: introducing expect_*() methods for page verification, using @property for reusable locators, returning page objects from actions where appropriate (fluent interface), removing unused helper methods and keeping the framework intentionally lightweight instead of overengineering it. <br>
**My Decision**: I accepted most of the suggestions, including introducing expect_*() methods, improving naming consistency and simplifying the public API. However I rejected tips that included changing the code's logic significantly (2+ files).

## Step 5️⃣ - final clean-up and architecture review
**Prompt**: "All three tests pass so now I would like to clean up the project before submitting. Please review my conftest.py - I have a feeling that the fixtures do too much. Point out anything that is redundant, misleading or hidden, and explain the reasoning rather than rewriting the code for me." <br>
**Response**: The model pointed out that my inventory_page fixture was doing two things at once - logging in and returning a page object - which meant the e2e test logged in twice: once through the fixture and once explicitly in the test body. It also noticed that the module docstring authentication was performed explicitly in the tests, which was no longer true, and that a commented-out version of the fixture was still left in the file. It suggested splitting the fixture into a separate, explicitly named logged_in fixture, so that every test declares in its own signature whether it needs a session. <br>
**My Decision**: I accepted it and split the fixtures. The refactor immediately broke the sorting test, because it had silently relied on the fixture logging in for it - the browser stayed on about:blank. Adding logged_in to the test signature fixed it. I kept the change: the failure was exactly the point, since the dependency was previously invisible from the test itself. I also removed the dead commented-out fixture. <br>

**A separate false alarm during the same clean-up**: at one point every test started failing with "Cannot navigate to invalid URL". It looked like a regression caused by the refactor, but the actual reason was that I run pytest from the parent directory, so pytest.ini was never loaded and --base-url was missing. The unknown-marker warnings in the output were the giveaway - the entire config file had been ignored, not just the base URL.

## Summary - where AI helped and where it did not
The model was strongest at structure: project layout, fixtures, CI configuration and naming conventions came back coherent and needed almost no correction. It was weakest wherever the answer depended on the real application - the locator bug in Step 2 is a good example, because the generated code looked correct and could never have worked. Every locator had to be verified against the running site, and the debugging steps above took more time than writing the tests themselves. 
