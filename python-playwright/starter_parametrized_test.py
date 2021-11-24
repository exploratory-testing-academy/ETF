import pytest
from playwright.sync_api import Page

url = "https://www.exploratorytestingacademy.com/app/"

def this_is_sample(): 
    with open('sample.txt') as f:
        lines = f.readlines()
    return str(lines)


@pytest.mark.parametrize('input_text, expect_wordcount, expect_discouraged, expect_violation', 
[
    ("To be or not to be - Hamlet's dilemma", 9, 2, 1)
])
def test_parametrized_test(page: Page, input_text, expect_wordcount, expect_discouraged, expect_violation):
    page.goto(url)
    page.fill("#inputtext", input_text)
    page.click("#CheckForEPrimeButton")
    assert page.inner_text("#wordCount") == str(expect_wordcount)
    assert page.inner_text("#discouragedWordCount") == str(expect_discouraged)
    assert page.inner_text("#possibleViolationCount") == str(expect_violation)
