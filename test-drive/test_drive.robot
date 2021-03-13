*** Settings ***
Library             Browser
Library             String
Test Setup          Default Setup
Test Teardown       Default Teardown
Test Template       Enter some text and count
*** Variables ***
${Test_Text}  Quick brown fox jumps over the lazy dog
${Long_Text}  Generate Random String  10000   [LETTERS]

*** Test Case ***

#First  ${Test_Text}  8  0  0
#Second  To be, or not to be  6  2  0
#Third  because  1  0  0
#Possessive  Eva's   1   0  1
Random  ${Long_Text}  1  0  0

*** Keywords ***
Enter some text and count
    [Arguments]  ${Text}  ${Word Count}  ${Discouraged Count}  ${Possible Violation Count}
    Log         ...nothing is here
    New Page   https://www.exploratorytestingacademy.com/app/
    fill text  css=#inputtext  ${Text}
    click       css=#CheckForEPrimeButton
    get text    css=#eprimeoutput  contains  ${Text}
    get text    css=#wordCount  ==  ${Word Count}
    get text    css=#discouragedWordCount  ==  ${Discouraged Count}
    get text    css=#possibleViolationCount  ==  ${Possible Violation Count}
Default Setup
    New Browser            chromium    headless=${false}
Default Teardown
    Close Browser