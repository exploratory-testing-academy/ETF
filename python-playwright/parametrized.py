import pytest
from playwright.sync_api import Page

url = "https://www.exploratorytestingacademy.com/app/"

def this_is_sample(): 
    with open('sample.txt') as f:
        lines = f.readlines()
    return str(lines)

data = [
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
    (this_is_sample(), 507, 2, 0), 
    #("The sky is blue", 4, 1, 0),
    #("Theskyisblue", 4, 1, 0),
    #("You're pretty", 3, 1, 0),
    #("one\ntwo", 2, 0, 0),
    #("Eeva\'s", "1", "0", "1"),
    #("<div>hello</div>", "1", "0", "0"),
    #("hello "*1000, "1000", "0", "0"),
    #("hello"*1000, "1", "0", "0"),
]


@pytest.mark.parametrize('input_text, expect_wordcount, expect_discouraged, expect_violation', data)
def test_parametrized_test(page: Page, input_text, expect_wordcount, expect_discouraged, expect_violation):
    page.goto(url)
    page.fill("#inputtext", input_text)
    page.click("#CheckForEPrimeButton")
    assert page.inner_text("#wordCount") == str(expect_wordcount)
    assert page.inner_text("#discouragedWordCount") == str(expect_discouraged)
    assert page.inner_text("#possibleViolationCount") == str(expect_violation)

