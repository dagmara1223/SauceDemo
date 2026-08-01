from __future__ import annotations
from playwright.sync_api import Locator, expect
from layouts.base_layout import BasePage, slug_name, to_float
from typing import Literal

SortOption = Literal["az", "za", "lohi", "hilo"]

class InventoryPage(BasePage):
    url = "/inventory.html"

    @property
    def items(self) -> Locator:
        return self.page.get_by_test_id("inventory-item")

    @property
    def item_names(self) -> Locator:
        return self.page.get_by_test_id("inventory-item-name")

    @property
    def item_prices(self) -> Locator:
        return self.page.get_by_test_id("inventory-item-price")

    @property
    def sort_dropdown(self) -> Locator:
        return self.page.get_by_test_id("product-sort-container")

    def open(self) -> "InventoryPage":
        """Loads inventory page"""
        self.page.goto(self.url)
        return self.expect_loaded()

    def expect_loaded(self) -> "InventoryPage":
        """page correctly loaded, items are available"""
        expect(self.page).to_have_url(self.url)
        expect(self.items.first).to_be_visible()
        return self

    def product_names(self) -> list[str]:
        """item names"""
        return [name.strip() for name in self.item_names.all_text_contents()]

    def product_prices(self) -> list[float]:
        """item prices converted into list of floats """
        return [to_float(price) for price in self.item_prices.all_text_contents()]

    def price_of(self, product_name: str) -> float:
        """item prices"""
        card = self.items.filter(has_text=product_name).first
        return to_float(
            card.get_by_test_id("inventory-item-price").inner_text()
        )

    def sort_by(self, option: SortOption) -> "InventoryPage":
        self.sort_dropdown.select_option(option)
        expect(self.sort_dropdown).to_have_value(option)
        return self

    def add_to_cart(self, product_name: str) -> "InventoryPage":
        """adding items to cart"""
        slug = slug_name(product_name)

        self.page.get_by_test_id(
            f"add-to-cart-{slug}"
        ).click()

        expect(
            self.page.get_by_test_id(f"remove-{slug}")
        ).to_be_visible()

        return self
    
