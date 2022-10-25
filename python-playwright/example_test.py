from playwright.sync_api import Page, expect

def test_example(page: Page):
    page.goto("https://www.exploratorytestingacademy.com/app/")
    page.locator('#inputtext').fill("To be or not to be - Hamlet's Dilemma")
    page.locator('#CheckForEPrimeButton').click()

    #BUG: Wordcount should be 8
    expect(page.locator("#wordCount")).to_have_text("9")
    expect(page.locator("#discouragedWordCount")).to_have_text("2")
    expect(page.locator("#possibleViolationCount")).to_have_text("1")