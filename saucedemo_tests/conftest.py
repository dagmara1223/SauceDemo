"""Shared pytest fixtures.

Each fixture provides a page object instance.
Authentication is performed explicitly in the tests to keep
each scenario independent and easy to understand.
"""

from __future__ import annotations

import pytest
from playwright.sync_api import Page
from layouts.login_layout import LoginPage
# from layouts.cart_layout import CartPage
# from layouts.checkout_layout import CheckoutPage
# from layouts.inventory_layout import InventoryPage

@pytest.fixture(scope="session", autouse=True)
def use_data_test_attribute(playwright):
    """SauceDemo exposes hooks as data-test, not Playwright's default data-testid."""
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Return the login page object."""
    return LoginPage(page)


# @pytest.fixture
# def inventory_page(page: Page) -> InventoryPage:
#     """Return the inventory page object."""
#     return InventoryPage(page)


# @pytest.fixture
# def cart_page(page: Page) -> CartPage:
#     """Return the cart page object."""
#     return CartPage(page)


# @pytest.fixture
# def checkout_page(page: Page) -> CheckoutPage:
#     """Return the checkout page object."""
#     return CheckoutPage(page)