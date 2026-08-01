"""Test 2 - the application rejects logins it is supposed to reject."""

import pytest
from data.users import LOCKED_OUT_USER, STANDARD_USER, User

LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
BAD_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
MISSING_PASSWORD = "Epic sadface: Password is required"

@pytest.mark.negative
@pytest.mark.parametrize(
    "user, expected_error",
    [
        pytest.param(
            LOCKED_OUT_USER,
            LOCKED_OUT,
            id="locked-out-account",
        ),
        pytest.param(
            User("standard_user", "wrong_password"),
            BAD_CREDENTIALS,
            id="wrong-password",
        ),
        pytest.param(
            User("standard_user", ""),
            MISSING_PASSWORD,
            id="empty-password",
        ),
    ],
)
def test_login_is_rejected(login_page, user: User, expected_error: str):
    (
        login_page
        .open()
        .login(user.username, user.password)
        .login_rejected(expected_error)
    )