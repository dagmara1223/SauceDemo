# SauceDemo - AI Assisted test automation 
Three automated tests for [saucedemo.com](https://www.saucedemo.com/) written using: 
- Python 🐍
- pytest 📝
- Playwright 📱<br>          
and built with AI Assistance. Purpose: Recruitment task. 


Important additional **.md** files: 
| Document | What is inside |
| --- | --- |
| [prompts.md](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/prompts.md) | Full prompt log - what I asked, what came back, and what had to be corrected |
| [approach.md](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/approach.md) | Why these three tests, how the project is structured, metrics, limitations |

## How to start 
---
The project root is `saucedemo_tests/` - `pytest.ini` lives there, so pytest has to be run from that folder. <br>
### Windows (PowerShell)
```powershell
git clone https://github.com/dagmara1223/SauceDemo.git
cd SauceDemo/saucedemo_tests
code .   # if opening using cmd 
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium

pytest
```

If PowerShell refuses to run the activation script, allow it for the current session only:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
---
### macOS / Linux
```bash
git clone https://github.com/dagmara1223/SauceDemo.git
cd SauceDemo/saucedemo_tests

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium

pytest
```
---

## Running the tests

```bash
pytest  # all 3 tests (8 cases)
pytest -m e2e  # the whole purchase flow/journey
pytest -m negative # login rejection cases
pytest -m data # sorting checks
pytest --durations=0 # timing of every test
```

If You want to see the browser doing the work use following flags: <br>
```
pytest -m e2e --headed
pytest -m negative --headed
pytest -m data --headed
```

Markers are registered in `pytest.ini`, so `--strict-markers` will catch a typo instead of silently skipping a test.

When something fails, a screenshot, a video and a Playwright trace land in `test-results/`. The trace is the useful one:
```bash
playwright show-trace test-results/<test-name>/trace.zip
```

---

## The three tests

| Test | What it verifies | Marker |
| --- | --- | --- |
| [test_login_negative.py](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/tests/test_login_negative.py) | Locked out account, wrong password and empty password are rejected - with the exact error message, and without letting the user past the login page | `negative` |
| [test_sorting_product.py](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/tests/test_sorting_product.py) | All four sorting options really reorder the data, and never lose or duplicate a product | `data` |
| [test_checkout.py](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/tests/test_checkout.py) | Full purchase journey, including whether the tax and the total match the prices shown on the inventory page | `e2e` |

Three tests, three different **kinds of risk**. The reasoning behind that choice - and behind what I deliberately left out - is in [approach.md](https://github.com/dagmara1223/SauceDemo/blob/main/saucedemo_tests/approach.md).

---

## Structure

```
saucedemo_tests/
├── layouts/                # page objects, all locators live here
│   ├── base_layout.py
│   ├── login_layout.py
│   ├── inventory_layout.py
│   ├── cart_layout.py
│   └── checkout_layout.py
├── data/                   # test data: users, products
├── tests/                  # assertions only
├── conftest.py             # shared fixtures (page objects + logged_in)
├── pytest.ini              # base URL, markers, artifacts on failure
├── requirements.txt
├── prompts.md
└── approach.md
```

Every locator uses the application's own `data-test` hooks, and there is also no `sleep()` anywhere - all waiting goes through Playwright's `expect()`. 

---

## CI
<img width="800" height="430" alt="image" src="https://github.com/user-attachments/assets/bda6ee50-2432-40e0-a57e-8cf7ea576fc2" /> <br>
The suite runs on GitHub Actions on every push, against the live site. Screenshots, videos and traces are uploaded as artifacts whenever a test fails. 
