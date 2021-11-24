import pytest
from playwright.sync_api import Page

def test_example(page: Page):
    page.goto("https://www.exploratorytestingacademy.com/app/")
