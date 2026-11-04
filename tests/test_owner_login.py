"""Authentication smoke tests, using fake credentials only."""
from pathlib import Path

import pytest

pytest.importorskip("streamlit")
bcrypt = pytest.importorskip("bcrypt")
from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parents[1] / "main.py")
TEST_EMAIL = "test-owner@example.invalid"
TEST_PASSWORD = "a-fake-test-password-not-a-real-secret"


def login_app():
    app = AppTest.from_file(APP, default_timeout=30)
    app.secrets["owner"] = {
        "email": TEST_EMAIL,
        "password_hash": bcrypt.hashpw(TEST_PASSWORD.encode(), bcrypt.gensalt(rounds=4)).decode(),
    }
    app.run()
    assert not list(app.exception), [str(e.message) for e in app.exception]
    return app


def submit_login(app, email, password):
    email_input = next(item for item in app.text_input if item.label == "Email")
    password_input = next(item for item in app.text_input if item.label == "Password")
    email_input.set_value(email)
    password_input.set_value(password)
    login_button = next(item for item in app.button if item.label == "Log in")
    login_button.click().run()
    assert not list(app.exception), [str(e.message) for e in app.exception]
    return app


def test_wrong_password_does_not_unlock_dashboard():
    app = submit_login(login_app(), TEST_EMAIL, "wrong-password")
    assert not app.session_state["owner_logged_in"]
    assert any("Incorrect email or password" in str(e.value) for e in app.error)

def test_correct_password_unlocks_dashboard():
    app = submit_login(login_app(), TEST_EMAIL.upper(), TEST_PASSWORD)
    assert app.session_state["owner_logged_in"]
    assert any("Welcome to Dashboard" in str(item.value) for item in app.markdown)


def test_logging_out_removes_owner_access():
    app = submit_login(login_app(), TEST_EMAIL, TEST_PASSWORD)
    logout_button = next(item for item in app.button if item.label == "Log out")
    logout_button.click().run()
    assert not app.session_state["owner_logged_in"]
