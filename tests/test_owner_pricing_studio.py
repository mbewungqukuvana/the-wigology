"""Test the real Pricing Studio through a small Streamlit test-only entry point."""
from pathlib import Path

import pytest

pytest.importorskip("streamlit")
from streamlit.testing.v1 import AppTest

HARNESS = str(Path(__file__).resolve().parent / "pricing_harness.py")


def launch():
    app = AppTest.from_file(HARNESS, default_timeout=30).run()
    assert not list(app.exception), [str(e.message) for e in app.exception]
    return app


def rendered(app):
    return "\n".join(str(element.value) for element in app.markdown)


def test_default_price_and_deposit_are_mathematically_consistent():
    app = launch()
    text = rendered(app)
    # Default: 2x20-inch ($85 each), 1x22-inch ($100), 18-inch 6x6 closure ($85).
    # Total: (355 + 65) * 18 + 200 + 330 = R8,090.
    # 35% gross margin => selling price = 8090 / .65 = R12,446.15.
    assert "8,090.00" in text
    assert "12,446.15" in text
    assert "7,467.69" in text  # 60% deposit
    assert "4,978.46" in text  # 40% balance


def test_unquoted_closure_blocks_the_selling_price():
    app = launch()
    app.button(key="pricing_tile_closure_9x6").click().run()
    assert not list(app.exception), [str(e.message) for e in app.exception]
    assert any("closure quote is missing" in str(e.value).lower() for e in app.error)
    assert "SUGGESTED SELLING PRICE" not in rendered(app)


def test_increasing_margin_changes_selling_price_not_underlying_cost():
    app = launch()
    app.button(key="pricing_margin_increase").click().run()
    assert not list(app.exception), [str(e.message) for e in app.exception]
    text = rendered(app)
    assert "8,090.00" in text  # underlying cost remains unchanged
    assert "13,483.33" in text  # 40% gross margin: 8090 / .60
