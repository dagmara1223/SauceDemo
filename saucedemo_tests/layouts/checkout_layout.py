from __future__ import annotations
from playwright.sync_api import Locator, expect
from layouts.base_layout import BasePage, to_float
import re

class CheckoutPage(BasePage):
    """Page object covering the entire checkout flow."""
    url = "/checkout-step-one.html"

    # Checkout: Your Information step
    @property
    def first_name(self) -> Locator:
        return self.page.get_by_test_id("firstName")

    @property
    def last_name(self) -> Locator:
        return self.page.get_by_test_id("lastName")

    @property
    def postal_code(self) -> Locator:
        return self.page.get_by_test_id("postalCode")

    @property
    def continue_button(self) -> Locator:
        return self.page.get_by_test_id("continue")

    def expect_information_step(self) -> "CheckoutPage":
        """Verify that the information form is displayed."""
        expect(self.page).to_have_url(self.url)
        expect(self.continue_button).to_be_visible()
        return self

    def fill_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> "CheckoutPage":
        """Fill customer info and continue to overview"""

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

        self.continue_button.click()

        return self.expect_overview_step()

    # Checkout: Overview step
    @property
    def finish_button(self) -> Locator:
        return self.page.get_by_test_id("finish")

    def expect_overview_step(self) -> "CheckoutPage":
        expect(self.page).to_have_url(
            re.compile(r".*/checkout-step-two\.html$")
        )
        expect(self.finish_button).to_be_visible()
        return self

    def tax(self) -> float:
        return self._money(
            self.page.get_by_test_id("tax-label").inner_text()
        )

    def total(self) -> float:
        return self._money(
            self.page.get_by_test_id("total-label").inner_text()
        )

    def finish(self) -> "CheckoutPage":
        """Complete the purchase."""
        self.finish_button.click()
        return self.expect_complete()

    # Checkout: Complete! step
    @property
    def complete_header(self) -> Locator:
        return self.page.get_by_test_id("complete-header")

    def expect_complete(self) -> "CheckoutPage":
        """verify that the order has been completed successfully."""
        expect(self.page).to_have_url(
            re.compile(r".*/checkout-complete\.html$")
        )
        expect(self.complete_header).to_be_visible()
        expect(self.complete_header).to_have_text(
            "Thank you for your order!"
        )

        # successful checkout should empty the cart to 0
        self.expect_cart_count(0)

        return self

    @staticmethod
    def _money(label: str) -> float:
        return to_float(label.split("$")[-1])