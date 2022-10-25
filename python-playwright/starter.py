import pytest
from playwright.sync_api import Page, expect

def test_example(page: Page):
    page.goto("https://www.exploratorytestingacademy.com/app/")
 