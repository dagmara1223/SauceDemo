### 1. Chronological record of prompt logs
A chronological record of the AI-assisted workflows using **Claude**, conversational mode. This section covers: what was asked, the reponse 
and how the response was corrected. 

## Step 0️⃣ - initialization
**Prompt**: "Hello, I am facing the task where I sould create AI-automized tests and maximize the quality of the result. I am explicitly asking for 
strategy, not an implementation. Which three test would You recommend to use on mini-Internet shop site with login, items that we could add to cart, 
finalize payments? We also have hamburger left-slide as feature, we can sort the products by the Name or Price, and we are provided with List of accepted
usernames to LogIn and usernames that were blocked / excluded."    
**Response**: AI Agent pointed out that we should focus on mentioned : 1. login trap, 2. create full flow: logging -> adding items (preferably 2+) -> cart -> summary 
-> payment / acceptance and 3. hamburger slide.   
**My Decision**: I accepted two provided examples: 1. and 2. but decided to go with product sorting check as 3. and describe lack of Slide Menu tests in **approach.md**. (link)

## Step 1️⃣ - first page
**Prompt**: "I have created the BasePage class from which all page objects inherit. I also 
created our first Login page + tests. Please suggest a maintainable project infrastructure for a Playwright + Pytest framework, including conftest.py, reusable fixtures, authentication handling, CI and project documentation. Focus on architecture rather than implementation"      
**Response**: AI Agent proposed a project structure similar to my initial design, including reusable pytest fixtures, centralized configuration (pytest.ini), a dedicated conftest.py and project documentation. It also suggested a more advanced authentication mechanism based on Playwright's storage_state, where the user logs       
**My Decision**: I accepted the response and decided to add GitHub Actions. However, I have
also decided not to proceed with storage_state idea since this specific task requires only
three tests, performing a fresh login in each relevant test adds execution time and code
becomes more complex.

## Step 2️⃣ - debugging 
**Propmt**: "Test login negative fail after the initial implementation. Help me identify the root cause - why is it failing? Explain what should be verified first and whether the problem seems to be correlated to bug in test or rather login page.       
**Response**: AI Agent suggested path that helped me with the debugging. It identified several possible causes, including incorrect page locators, project import structure, inconsistent naming introduced during refactoring (URL vs url) and finally incorrect expected assertion values.        
**My Decision/Resolution**: The issue was, in fact, correlated to misspeling "url" and using 
"URL" everywhere, and also some other minor bugs like using non-relevant functions that work with my version of playwright. After that - all 3 passed.

## Step   - debugging
**Prompt**: "The tests fail even though the elements are visible in the browser and playwright reports that the locator cannot find the element. Help me identify whether the issue is related to the locator strategy, the application itself or the Playwright configuration. Explain the reasoning and where to look for the bug."
**Response**: AI suggested verifying whether the application used Playwright's default data-testid attribute or a custom attribute - SauceDemo exposes testing hooks as data-test, while get_by_test_id() expects data-testid unless configured otherwise.
**My Decision**: AI was right, the bug was from my side. I implemented following line: 
playwright.selectors.set_test_id_attribute("data-test")

## Step  - when work was done
**Prompt**: "Please review my current logic and implementation. The tests are working fine,
all 3 of them: e2e, data and negative (test for login). Focus on InventoryPage, CartPage and CheckoutPage - on maintainability, spelling, fluent usage, correct variable names, and whether the public API of each page is coherent. Please don't change the code, just give me some finishing touches tips"
**Response**: Several improvements were suggested: ntroducing expect_*() methods for page verification, using @property for reusable locators, returning page objects from actions where appropriate (fluent interface), removing unused helper methods and keeping the framework intentionally lightweight instead of overengineering it.
**My Decision**: I accepted most of the suggestions, including introducing expect_*() methods, improving naming consistency and simplifying the public API. However I rejected tips that included changing the code's logic significally (2+ files).
