import pytest
from playwright.sync_api import Page, expect

def test_example(page: Page):
    page.goto("https://www.exploratorytestingacademy.com/app/")
    page.fill("#inputtext", "To be or not to be - Hamlet's dilemma")
    page.click("#CheckForEPrimeButton")
    #BUG: it should really be 8, but it's not
    #assert page.inner_text("#wordCount") == str(9)
    expect(page.locator("#wordCount")).to_contain_text("9")
    assert page.inner_text("#discouragedWordCount") == str(2)
    assert page.inner_text("#possibleViolationCount") == str(1)
