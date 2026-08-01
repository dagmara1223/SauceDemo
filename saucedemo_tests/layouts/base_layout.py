# Here we create Base Class Page that will be inherited by each page object

from __future__ import annotations
import re
from playwright.sync_api import Locator, Page, expect

def to_float(price_str: str) -> float:
    """
    Converts string prices to floats: $29.99 -> 29.99
    """
    return float(price_str.replace("$", "").strip())

def slug_name(product_name: str) -> str:
    """
    Converst a product name, like: Sauce Labs Backpack to saucedemo format: sauce-labs-backpack.
    """
    return re.sub(r"[^a-z0-9]+", "-", product_name.lower()).strip("-")

class BasePage:
    """Behaviour expected by every page object."""

    def __init__(self, page: Page):
        self.page = page

    # header ----------
    @property
    def cart_link(self) -> Locator: # creates locator to shopping cart icon
        return self.page.get_by_test_id("shopping-cart-link")

    @property
    def cart_badge(self) -> Locator:  # creates locator to circle with amount of products
        return self.page.get_by_test_id("shopping-cart-badge")

    def open_cart(self) -> None: 
        """Open the shopping cart."""
        self.cart_link.click()
        expect(self.page).to_have_url(re.compile(r".*/cart\.html$"))

    def expect_cart_count(self, count:int) -> None:
        """
        Assert the number displayed on the shopping cart badge. Exception: if 0, in Sauce it is not 
        displayed - We will only see cart icon but without the number.
        """
        if count > 0:
            expect(self.cart_badge).to_have_text(str(count))
        else:
            expect(self.cart_badge).to_have_count(0)

    # burger ----------
    @property
    def menu_button(self) -> Locator:
        return self.page.locator("#react-burger-menu-btn")

    @property
    def logout_button(self) -> Locator:
        return self.page.get_by_test_id("logout-sidebar-link")
    
    @property
    def reset_app_state_button(self) -> Locator:
        return self.page.get_by_test_id("reset-sidebar-link")

    def open_menu(self) -> None:
        """Expand the left-side navigation menu."""
        self.menu_button.click()
        expect(self.logout_button).to_be_visible()

    def logout(self) -> None:
        """Log out and verify that the login page is displayed."""
        self.open_menu()
        self.logout_button.click()

        expect(self.page).to_have_url(re.compile(r".*/$"))
        expect(self.page.get_by_test_id("login-button")).to_be_visible()


    