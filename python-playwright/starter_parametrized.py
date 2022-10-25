import pytest
from playwright.sync_api import Page, expect

url = "https://www.exploratorytestingacademy.com/app/"

def this_is_sample(): 
    with open('sample.txt') as f:
        lines = f.readlines()
    return str(lines)


@pytest.mark.parametrize('input_text, expect_wordcount, expect_discouraged, expect_violation',
[
    ("word", "1", "0", "0")
])
def test_parametrized_test(page: Page, input_text, expect_wordcount, expect_discouraged, expect_violation):
    page.goto(url)
    page.fill("#inputtext", input_text)
    page.click("#CheckForEPrimeButton")
    expect(page.locator('#eprimeoutput')).to_have_text(input_text)
    expect(page.locator("#wordCount")).to_have_text(str(expect_wordcount))
    expect(page.locator("#discouragedWordCount")).to_have_text(str(expect_discouraged))
    expect(page.locator("#possibleViolationCount")).to_have_text(str(expect_violation))
