import pytest
from playwright.sync_api import Page, expect

url = "https://www.exploratorytestingacademy.com/app/"

def this_is_sample(): 
    with open('sample.txt') as f:
        lines = f.readlines()
    return str(lines)


@pytest.mark.parametrize('input_text, expect_wordcount, expect_discouraged, expect_violation',
[
    ("word", "1", "0", "0"),
    ("If programming's the act of teaching a computer to have a conversation with a user, it most useful to first teach the computer how to speak.","26","0","1"),
    #bug: incorrectly recognized - should be recognized and isn't. 
    #("you're","2","1","0"),
    #("be\nare\nis", "3", "3", "0"), #bug
    ("\"be\"", "1", "1", "0"),
    #("'be'", "1", "1", "0") #bug
])
def test_parametrized_test(page: Page, input_text, expect_wordcount, expect_discouraged, expect_violation):
    page.goto(url)
    page.locator("#inputtext").fill(input_text)
    page.locator("#CheckForEPrimeButton").click()
    expect(page.locator('#eprimeoutput')).to_have_text(input_text)
    expect(page.locator("#wordCount")).to_have_text(str(expect_wordcount))
    expect(page.locator("#discouragedWordCount")).to_have_text(str(expect_discouraged))
    expect(page.locator("#possibleViolationCount")).to_have_text(str(expect_violation))
