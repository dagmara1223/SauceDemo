"""Test 1 - complete purchase journey."""

import pytest

from data.products import BACKPACK, BIKE_LIGHT, BOLT_T_SHIRT, FLEECE_JACKET, ONESIE
from data.users import STANDARD_USER

PRODUCTS = [BACKPACK, BIKE_LIGHT, BOLT_T_SHIRT, FLEECE_JACKET, ONESIE]
TAX_RATE = 0.08

@pytest.mark.e2e
def test_complete_purchase_journey(
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
):
    # Login to page using standard_user
    (
        login_page
        .open()
        .login(STANDARD_USER.username, STANDARD_USER.password)
        .login_passed()
    )

    inventory_page.expect_loaded()

    # Add products
    expected_prices = {
        product: inventory_page.price_of(product)
        for product in PRODUCTS
    }

    for product in PRODUCTS:
        inventory_page.add_to_cart(product)

    inventory_page.expect_cart_count(len(PRODUCTS))

    # Cart
    inventory_page.open_cart()
    cart_page.expect_loaded()

    assert sorted(cart_page.item_names()) == sorted(PRODUCTS)
    assert sorted(cart_page.item_prices()) == sorted(expected_prices.values())

    # Checkout
    cart_page.checkout()
    checkout_page.expect_information_step()

    (
        checkout_page
        .fill_information(
            "Dagmara",
            "Krenich",
            "30-001",
        )
    )

    expected_total = round(sum(expected_prices.values()), 2)

    assert checkout_page.tax() == pytest.approx(
        round(expected_total * TAX_RATE, 2),
        abs=0.01,
    )

    assert checkout_page.total() == pytest.approx(
        expected_total + checkout_page.tax(),
        abs=0.01,
    )
    (
        checkout_page
        .finish()
        .expect_complete()
    )