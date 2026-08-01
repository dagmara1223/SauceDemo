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
