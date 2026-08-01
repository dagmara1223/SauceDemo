from __future__ import annotations
import re
from playwright.sync_api import Locator, expect
from layouts.base_layout import BasePage

class LoginPage(BasePage):
    url="/"

    @property
    def username(self) -> Locator:
        return self.page.get_by_test_id("username")

    @property
    def password(self) -> Locator:
        return self.page.get_by_test_id("password")

    @property
    def error(self) -> Locator:
        return self.page.get_by_test_id("error")

    @property
    def login_button(self) -> Locator:
        return self.page.get_by_test_id("login-button")

    def open(self) -> "LoginPage":
        "open the login page and wait till its ready."
        self.page.goto(self.url)
        expect(self.login_button).to_be_visible()
        return self

    def login(self, username: str, password:str) -> "LoginPage":
        "Login using the provided username and password"
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        return self

    def login_passed(self) -> "LoginPage":
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html$"))
        return self

    def login_rejected(self, text:str)-> "LoginPage":
        expect(self.error).to_be_visible()
        expect(self.error).to_have_text(text)
        # A rejected login must not leak past the gate.
        expect(self.page).not_to_have_url(re.compile(r".*/inventory\.html$"))
        return self
