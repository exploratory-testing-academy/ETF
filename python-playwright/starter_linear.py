import pytest
from playwright.sync_api import Page, expect

def test_example(page: Page):
    page.goto("https://www.exploratorytestingacademy.com/app/")
    page.fill("#inputtext", "word")
    page.click("#CheckForEPrimeButton")
    expect(page.locator("#wordCount")).to_have_text("1")
    expect(page.locator("#discouragedWordCount")).to_have_text("0")
    expect(page.locator("#possibleViolationCount")).to_have_text("0")
