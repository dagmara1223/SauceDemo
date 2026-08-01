"""Test 3 - verify that product sorting changes only the order of items."""
import pytest

SORTING_OPTIONS = [
    pytest.param("az", "names", False, id="name-a-to-z"),
    pytest.param("za", "names", True, id="name-z-to-a"),
    pytest.param("lohi", "prices", False, id="price-low-to-high"),
    pytest.param("hilo", "prices", True, id="price-high-to-low"),
]

@pytest.mark.data
@pytest.mark.parametrize("option, field, reverse", SORTING_OPTIONS)
def test_sorting_orders_the_product_list(
    inventory_page,
    option,
    field,
    reverse,
):
    inventory_page.expect_loaded()

    original_products = set(inventory_page.product_names())

    inventory_page.sort_by(option)

    if field == "names":
        values = inventory_page.product_names()
    else:
        values = inventory_page.product_prices()

    assert values == sorted(values, reverse=reverse)
    assert set(inventory_page.product_names()) == original_products