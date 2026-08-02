"""Shared pytest fixtures.

Page object fixtures return bare objects. Authentication is a separate,
explicitly named fixture, so each test states whether 
it needs a session.
"""

from __future__ import annotations

import pytest
from playwright.sync_api import Page
from layouts.login_layout import LoginPage
from layouts.cart_layout import CartPage
from layouts.checkout_layout import CheckoutPage
from layouts.inventory_layout import InventoryPage
from data.users import STANDARD_USER

@pytest.fixture(scope="session", autouse=True)
def use_data_test_attribute(playwright):
    """SauceDemo exposes hooks as data-test, not Playwright's default data-testid."""
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def logged_in(page: Page) -> Page:
    """Log in as the standard user and land on the inventory page."""
    (
        LoginPage(page)
        .open()
        .login(STANDARD_USER.username, STANDARD_USER.password)
        .login_passed()
    )
    return page

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Return the login page object."""
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """Return the inventory page object."""
    return InventoryPage(page)

@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)

@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)