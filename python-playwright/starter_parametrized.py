import pytest
from playwright.sync_api import Page, expect

url = "https://www.exploratorytestingacademy.com/app/"

def this_is_sample(): 
    with open('bible.txt') as f:
        lines = f.readlines()
    return str(lines)


@pytest.mark.parametrize('input_text, expect_wordcount, expect_discouraged, expect_violation',
[
    ("word", "1", "0", "0"),
    ("If programming's the act of teaching a computer to have a conversation with a user, it most useful to first teach the computer how to speak.","26","0","1"),     #bug: programming's is counted as two words when it is shortening for is-verb
    ("we're", "1", "1", "0"), #bug: 're incorrectly recognized - should be recognized and isn't.
    ("be\nare\nis", "3", "3", "0"), #bug miscalculation
    ("be \nare \nis", "3", "3", "0"), #bug extra space on grey area
    ("The whole new world !", "4", "0", "0"), #bug symbols surounded by space(s) are counted as words 
    ("Martha_@gmail.com", "1", "0", "0"),
    ("\"be\"", "1", "1", "0"),
    (10000*"be" , "1", "0", "0"), #bug doesn fit the grey box
    (10000*"be " , "10000", "10000", "0"), #bug: no vertical scrolling (fixed)
    ("'be'", "1", "1", "0"), #bug single quotes makes "be" unrecognizable
    (this_is_sample(), "31172", "21", "1")
])
def test_parametrized_test(page: Page, input_text, expect_wordcount, expect_discouraged, expect_violation):
    page.goto(url)
    page.locator("#inputtext").fill(input_text)
    page.locator("#CheckForEPrimeButton").click()
    expect(page.locator('#eprimeoutput')).to_have_text(input_text)
    expect(page.locator("#wordCount")).to_have_text(str(expect_wordcount))
    expect(page.locator("#discouragedWordCount")).to_have_text(str(expect_discouraged))
    expect(page.locator("#possibleViolationCount")).to_have_text(str(expect_violation))
