"""Checks the real catalog and supplier tables without launching Streamlit."""
import ast
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def assignment(filename, variable):
    """Read a literal value assigned in the app source, without running the UI."""
    tree = ast.parse((ROOT / filename).read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(t, ast.Name) and t.id == variable for t in node.targets):
                return ast.literal_eval(node.value)
    raise AssertionError(f"Missing expected constant: {variable}")


@pytest.mark.parametrize("filename", ["main.py", "pricing_studio.py"])
def test_python_files_have_valid_syntax(filename):
    compile((ROOT / filename).read_bytes(), filename, "exec")


def test_all_advertised_hair_types_have_profiles_and_photos():
    hair = assignment("main.py", "HAIR")
    photos = assignment("main.py", "HAIR_PHOTOS")
    origins = assignment("main.py", "hair_origins")
    assert set(hair) == set(origins)
    for origin, textures in hair.items():
        assert textures, f"No textures defined for {origin}"
        for texture, profile in textures.items():
            assert f"{origin} {texture}" in photos, f"Missing photo mapping for {origin} {texture}"
            assert all(profile.get(k) for k in ("about", "appearance", "sew_in", "wig", "care"))


def test_customer_pages_have_unique_url_slugs():
    pages = assignment("main.py", "CUSTOMER_PAGE_SLUGS")
    assert len(pages) == len(set(pages.values()))
    assert pages["Home"] == "home"


def test_supplier_bundle_quotes_are_positive_and_increase_with_length():
    indian = assignment("pricing_studio.py", "INDIAN_BUNDLES")
    filipino = assignment("pricing_studio.py", "FILIPINO_SAMPLE_BUNDLES")
    indian_prices = [row["Straight / Wavy"] for _, row in sorted(indian.items())]
    filipino_prices = [value for _, value in sorted(filipino.items())]
    for prices in (indian_prices, filipino_prices):
        assert all(price > 0 for price in prices)
        assert prices == sorted(prices), "Longer bundles have unexpectedly lower supplier quotes"


@pytest.mark.parametrize("constant", ["INDIAN_CLOSURES", "FILIPINO_CLOSURES"])
def test_closure_quotes_are_positive(constant):
    table = assignment("pricing_studio.py", constant)
    assert table
    assert all(price > 0 for row in table.values() for price in row.values())


def test_unquoted_closure_is_not_silently_given_an_invented_price():
    # The current supplier tables do not include a 9x6 quote.
    for constant in ("INDIAN_CLOSURES", "FILIPINO_CLOSURES"):
        table = assignment("pricing_studio.py", constant)
        assert all("9×6" not in row for row in table.values())


def test_no_local_secret_file_is_committed():
    import subprocess

    result = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        pytest.skip("Not running inside a Git checkout")
    forbidden = {"secrets.toml", ".env", ".env.production", ".env.local"}
    tracked = [name for name in result.stdout.splitlines() if Path(name).name in forbidden]
    assert not tracked, f"Secret files must not be tracked: {tracked}"
