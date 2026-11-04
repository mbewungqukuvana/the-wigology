"""True browser tests against a running local Streamlit server (Chromium)."""
import os

from playwright.sync_api import expect, sync_playwright

BASE_URL = os.environ.get("WIGOLOGY_TEST_URL", "http://127.0.0.1:8501")


def test_browser_wig_builder_quoted_and_unquoted_prices():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(BASE_URL, wait_until="domcontentloaded")
        build = page.get_by_role("button", name="BUILD YOUR DREAM WIG")
        expect(build).to_be_visible(timeout=30000)
        build.click()
        expect(page.get_by_text("Build Your Dream Wig", exact=True)).to_be_visible(timeout=30000)
        page.get_by_role("button", name="Indian", exact=True).click()
        page.get_by_role("button", name="Wavy", exact=True).click()
        page.get_by_role("button", name="6x6", exact=True).click()
        expect(page.get_by_text("R 12,030.77", exact=True)).to_be_visible(timeout=30000)
        page.get_by_role("button", name="9x6", exact=True).click()
        expect(page.get_by_text("Price on request", exact=True)).to_be_visible(timeout=30000)
        browser.close()


def test_mobile_storefront_can_open_shop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
        page.goto(BASE_URL, wait_until="domcontentloaded")
        shop = page.get_by_role("button", name="SHOP NOW")
        expect(shop).to_be_visible(timeout=30000)
        shop.click()
        expect(page.get_by_text("Shop Bundles & Closures.", exact=True)).to_be_visible(timeout=30000)
        browser.close()
