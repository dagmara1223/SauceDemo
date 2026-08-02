## Approach
### Choosing the three tests
Task allowed three tests, so I decided to test three different kinds of risk:

1. Negative login - marked as:
<img width="950" height="247" alt="image" src="https://github.com/user-attachments/assets/4dc9765c-eff8-479d-a8af-83006b928325" /> <br>
In this test we looked at locked out account, wrong password and empty password. I asserted exact error message and also that the User did not get past the login page. Asserting only "an error is visible" would still pass if the application showed the wrong message. <br>
**Source:** [test_login_negative.py](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/tests/test_login_negative.py)
2. Product sorting - marked as:
<img width="950" height="247" alt="image" src="https://github.com/user-attachments/assets/e3392a1b-93d1-4fec-ba68-e5a08467d452" /> <br>
We tested all four different sorting options (by price and by item name). I compared the rendered order with the list sorted locally, and additionally checked that the set of products did not change, because sorting must never lose or duplicate an item. <br>
**Source:** [test_sorting_product.py](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/tests/test_sorting_product.py) <br>
3. Finally - Complete E2E purchase journey, marked as:
<img width="950" height="247" alt="image" src="https://github.com/user-attachments/assets/1b1a9204-030f-46d1-b5a3-1101a896fea9" /> <br>
We tested the full flow: **login** -> **Add 5 items: BACKPACK, BIKE_LIGHT, BOLT_T_SHIRT, FLEECE_JACKET, ONESIE** -> **customer form information** -> **overview** -> **purchase complete**.
I additionally focused on the money part: I collected the prices displayed on the inventory page, and then checked that the tax and the total on the overview step match what those prices imply. <br>
**Source:** [test_checkout.py](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/tests/test_checkout.py) <br>


My first instinct was to test hamburger slide menu, but after confirming that it was mostly navigation - four links, four times the same kind of assertion, I decided **not** to. I chose to test sorting items instead, to verify that the application processes data correctly. For the same reason I did not build tests on problem_user, error_user or visual_user. They are broken by design, and the task requires tests that pass - a green test on a broken account means encoding current breakage as the expected result. ✅

### Structure 
<img width="313" height="800" alt="image" src="https://github.com/user-attachments/assets/1d02ec16-7cd4-4589-84f3-e6b4addd4f65" />
Page objects live in layouts/ and inherit from BasePage, test data (users, products) lives in data/, and tests/ contains assertions only. Every locator uses the application's own data-test hooks, so no XPath and no selectors coupled to styling. There is no sleep() anywhere - all waiting is done through Playwright's expect(), for example add_to_cart() waits for the button to change into "Remove", which is a real signal that the state changed.

Authentication is a separate logged_in fixture, not something hidden inside the page object fixtures. Tests that only need a session ask for it explicitly in their signature, while the e2e test performs the login in its own body - there the login is part of the scenario being tested, not setup. ✅ 

### Working with AI: 

