import pytest
from playwright.sync_api import Page

url = "https://www.exploratorytestingacademy.com/app/"

def this_is_file(text): 
    with open(text+'.txt') as f:
        lines = f.readlines()
    return str(lines)

@pytest.mark.parametrize('input_text, expect_wordcount, expect_discouraged, expect_violation', 
[
    #9 cases below pass but with a BUG
    ("To be or not to be - Hamlet's dilemma", 9, 2, 1),
    ("nothing", 1, 0, 0),
    ("to be or not to be", 6, 2, 0),
    ("", 0, 0, 0),
    ("be, being, been, am, is, isn't, are, aren't, was, wasn't, were, and weren't.", 13, 12, 0),
    ("\n", 1, 0, 0),
    ("I'm, you're, we're, they're, he's, she's, it's, there's, here's, where's, how's, what's, who's, aint's, that's.", 15, 1, 11 ), 
    ("first\nsecond", 1, 0, 0),
    ("ain't, amn't", 2, 2, 0),
    ("Hanna's Esa's Meera's Süëss-O'Reggio's or Okechukwu's", 6, 0, 4), 
    ("'be'", 1, 0, 0),
    ("human being", 2, 1, 0),
    ("typewriter's apostrophe", 2, 0, 1), 
    ("typesetter’s apostrophe", 2, 0, 0), 
    (1000 * "x", 0, 0, 0),
    (this_is_file('sample'), 508, 2, 0), 
    (this_is_file('bible'), 31172, 21, 1),
],
ids=['demo', 'not eprime', 'hamlet', 'empty', 'be in forms', 'newline', 'contractions', 'newline with words', 'slang', 'possessive', 'quoted be', 'not verb', 'typewriters apostrophe', 'typesetters apostrophe', 'long word', 'file', 'bible' ]
)

def test_parametrized_test(page: Page, input_text, expect_wordcount, expect_discouraged, expect_violation):
    page.goto(url)
    page.fill("#inputtext", input_text)
    page.click("#CheckForEPrimeButton")
    assert page.inner_text("#wordCount") == str(expect_wordcount)
    assert page.inner_text("#discouragedWordCount") == str(expect_discouraged)
    assert page.inner_text("#possibleViolationCount") == str(expect_violation)

