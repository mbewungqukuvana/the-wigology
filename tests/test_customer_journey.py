"""Run the actual Streamlit customer app, clicking real widgets."""
from pathlib import Path

import pytest

streamlit = pytest.importorskip("streamlit")
from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parents[1] / "main.py")


def launch(page="home"):
    app = AppTest.from_file(APP, default_timeout=30)
    app.query_params["page"] = page
    app.run()
    assert not list(app.exception), [str(e.message) for e in app.exception]
    return app


def click(app, key):
    app.button(key=key).click().run()
    assert not list(app.exception), [str(e.message) for e in app.exception]
    return app


def rendered(app):
    return "\n".join(str(element.value) for element in app.markdown)


def test_homepage_has_customer_entry_points():
    app = launch()
    assert app.button(key="homepage_build")
    assert app.button(key="homepage_shop")
    assert app.button(key="homepage_science")
    assert "Welcome to Dashboard" not in rendered(app)


def test_customer_can_build_a_quoted_indian_wavy_wig():
    app = launch("build-your-dream-wig")
    click(app, "wig_tile_origin_Indian")
    click(app, "wig_tile_texture_Wavy")
    click(app, "wig_tile_closure_size_6x6")
    text = rendered(app)
    assert "Indian Wavy" in text
    # Three 20-inch bundles at $85 each, an 18-inch 6x6 closure at $85,
    # plus $65 shipping, R200 customs, R330 making, R18/USD, 35% margin.
    assert "12,030.77" in text


def test_unquoted_nine_by_six_closure_shows_price_on_request():
    app = launch("build-your-dream-wig")
    click(app, "wig_tile_origin_Indian")
    click(app, "wig_tile_texture_Wavy")
    click(app, "wig_tile_closure_size_9x6")
    text = rendered(app)
    assert "Price on request" in text
    assert "12,030.77" not in text


def test_indian_curly_does_not_reuse_wavy_supplier_price():
    app = launch("build-your-dream-wig")
    click(app, "wig_tile_origin_Indian")
    click(app, "wig_tile_texture_Curly")
    click(app, "wig_tile_closure_size_6x6")
    assert "Price on request" in rendered(app)


def test_owner_dashboard_not_displayed_without_login():
    app = launch("home")
    assert "Welcome to Dashboard" not in rendered(app)
    assert not any("Owner tools" == getattr(radio, "label", "") for radio in app.radio)
