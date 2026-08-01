from __future__ import annotations
from playwright.sync_api import Locator, expect
from layouts.base_layout import BasePage, to_float

class CartPage(BasePage):
    url = "/cart.html"

    @property
    def items(self) -> Locator:
        """initialize cart location"""
        return self.page.get_by_test_id("inventory-item")
    
    @property
    def checkout_button(self) -> Locator:
        return self.page.get_by_test_id("checkout")

    @property
    def item_names_locator(self) -> Locator:
        return self.page.get_by_test_id("inventory-item-name")


    @property
    def item_prices_locator(self) -> Locator:
        return self.page.get_by_test_id("inventory-item-price")
 
    def open(self) -> "CartPage":
        self.page.goto(self.url)
        return self.expect_loaded()

    def expect_loaded(self) -> "CartPage":
        expect(self.page).to_have_url(self.url)
        expect(self.checkout_button).to_be_visible()
        return self

    def item_names(self) -> list[str]:
        return [
            name.strip() for name in self.item_names_locator.all_text_contents()
        ]

    def item_prices(self) -> list[float]:
        return [
            to_float(price) for price in self.item_prices_locator.all_text_contents()
        ]

    def checkout(self) -> None:
        self.checkout_button.click()