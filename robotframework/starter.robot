*** Settings ***
Library             Browser
Test Setup          Default Setup
Test Teardown       Default Teardown

*** Variables ***

*** Test Cases ***

This is a test
    New page  https://www.exploratorytestingacademy.com/app/


*** Keywords ***
Default Setup
    New Browser            chromium    headless=${FALSE}

Default Teardown
    Close Browser
