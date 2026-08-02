### Approach 

### Choosing the three tests 
Task allowed three tests, so I decided to test three different kinds of risk: <br>
1. Negative login - marked as :
<img width="950" height="257" alt="image" src="https://github.com/user-attachments/assets/c6c17041-024b-42c9-affb-3b1a597967ad" />  <br>
In this test we looked at locked out account, wrong password and empty password. I asserted exact error message and also that the User did not get past the login page. Asserting only "an error is visible" would still pass if the application showed the wrong message. <br>
**Source:** [test_login_negative.py](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/tests/test_login_negative.py)
