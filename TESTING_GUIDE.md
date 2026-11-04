# The Wigology — Advanced Testing Kit

These files are designed for the **current** `main.py` and `pricing_studio.py` you shared on 4 November 2026.

## What is included

- `tests/test_catalog_and_pricing_data.py`: catalog consistency, syntax, supplier quote sanity checks.
- `tests/test_customer_journey.py`: real Streamlit app tests for homepage, wig builder and missing-price cases.
- `tests/test_owner_pricing_studio.py`: verifies actual owner pricing, margin and deposit display.
- `tests/test_owner_login.py`: verifies login failures, successful login and logout using **fake** credentials.
- `tests_browser/test_browser.py`: real Chromium tests for wig pricing and mobile shopping navigation.
- `tests/pricing_harness.py`: a test-only way to run the owner's pricing tool without needing a real password.
- `.github/workflows/tests.yml`: automatic tests on pushes, pull requests, nightly and on demand.
- `requirements-test.txt`: packages needed for the tests.

## Installation

1. Unzip the kit and **copy its contents into the root of your existing `the-wigology` project**, merging folders. Do not replace your existing `main.py`, `pricing_studio.py`, or images.
2. In VS Code's terminal, from the project folder, run:

   ```bash
   python3 -m pip install -r requirements-test.txt
   python3 -m pytest -q tests/
   ```

   Browser tests run automatically in GitHub Actions. To run them locally, first start the app in another terminal with `python3 -m streamlit run main.py`, install Chromium with `python3 -m playwright install chromium`, then run `python3 -m pytest -q tests_browser/`.

3. Read any failure details. Red tests are useful: they identify mismatches to investigate, and are **not automatically proof of a bug**.
4. Once the tests run, commit and push the new files:

   ```bash
   git add .github/workflows/tests.yml requirements-test.txt tests/ tests_browser/
   git commit -m "Add advanced automated tests"
   git push origin main
   ```

5. Visit your GitHub repository's **Actions** tab. You can also run the workflow with **Run workflow**.

## Safety

- This kit does not change your original application source code.
- Never commit `.streamlit/secrets.toml`, real passwords or production API keys.
- These tests do not connect to a payment provider or place orders.
- Do not load-test your production Render server without setting safe limits.
- The owner login tests use a fake `.invalid` email address and a temporary bcrypt hash.

## Important limitations

- Streamlit and bcrypt could not be installed in the isolated file-building environment, so the **Streamlit UI, browser and authentication tests have not been executed here**. They must be verified on your Mac or GitHub Actions. Static tests were checked locally against the uploaded source files.
- These tests cover several real user flows, not all combinations or browsers. Browser-based Playwright tests are included but must be verified in GitHub Actions; production uptime monitoring is a separate next step.
- This kit's test-only dependencies do not replace the production `requirements.txt` needed by Render.
- GitHub Actions scheduled workflows may be delayed, and can be disabled under certain repository inactivity conditions.
