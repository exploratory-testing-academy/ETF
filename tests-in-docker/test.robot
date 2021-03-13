*** Settings ***
Library             Browser
Test Setup          Default Setup
Test Teardown       Default Teardown
Test Template       Verify Word Text

*** Variables ***
${URL}      https://www.exploratorytestingacademy.com/app/

*** Test Cases ***
Test1    nothing     1   0
Test2    to be or not to be      6   2
Test3    The cat is my only pet  6   1
Test4    The cat is Garfield     4   1
Test5    be, being, been, am, is, isn't, are, aren't, was, wasn't, were, and weren't.    13  12
Test6    I'm, you're, we're, they're, he's, she's, it's, there's, here's, where's, how's, what's, who's, aint's, that's.    15    15
Test7    ${EMPTY}    0   0

*** Keywords ***
Verify Word Text
    [Arguments]     ${input text}      ${word count}      ${discouraged count}
    New Page   ${URL}
    Fill Text       css=#inputtext  ${input text}
    Click   css=#CheckForEPrimeButton
    Get Text    css=#eprimeoutput   ==   ${input text}
    Get Text    css=#wordCount      ==   ${word count}
    Get Text    css=#discouragedWordCount  ==   ${discouraged count}

Default Setup
    New Browser            chromium    headless=${true}

Default Teardown
    Close Browser