import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize('input_text, expect_wordcount, expect_discouraged, expect_violation',
[
    ("it has to be 6 words", "6", "1", "0"),
    ("being human being is hard", "5", "2", "0"),
    ("it's to be 6 words", "5", "1", "1"),
    ("It is", "2", "1", "0"),
    ("it \n is", "2", "1", "0"),
    (" \n ", "0", "0", "0"),
    (" \n something", "1", "0", "0"),
    ("\n", "0", "0", "0"),
    ("!", "0", "0", "0"),
    ("A B C D", "4", "0", "0"),
    ("Pneumonoultramicroscopicsilicovolcanoconiosis", "1", "0", "0"),
    ("Pneumonoultramicroscopicsilicovolcanoconiosis"*300, "1", "0", "0"),
    ("Pneumonoultramicroscopicsilicovolcanoconiosis "*300 + "is", "301", "1", "0"),
    ("Pneumonoultramicroscopicsilicovolcanoconiosis "*3000 + "is", "3001", "1", "0"),
    ("Irja's", "1","0","1"),
    ("Eva's", "1","0","1"),
    ("Irja’s", "1","0","1"),
    ("Jean-Paul's", "1","0","1"),
    ("O'Raylye's", "1","0","1"),
    ("it\nis", "2", "1", "0"),
    ("we're", "1", "1", "0")
])
def test_example(page: Page, input_text, expect_wordcount, expect_discouraged, expect_violation):
    page.goto("https://www.exploratorytestingacademy.com/app/")
    page.fill('#inputtext', input_text)
    page.click('#CheckForEPrimeButton')

    expect(page.locator("#wordCount")).to_have_text(expect_wordcount)
    expect(page.locator("#discouragedWordCount")).to_have_text(expect_discouraged)
    expect(page.locator("#possibleViolationCount")).to_have_text(expect_violation)
