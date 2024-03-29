Feature: Eprime text analysis
    As a user,
    I want to verify my text for violations of eprime,
    So I learn to write proper English

    Scenario: Eprime analysis
        Given the eprime page is displayed
        When user analyses sentence to be or not to be
        Then user learns sentence has 2 be-verbs, 0 possible be-verbs and total 6 words

    Scenario: Incorrect Eprime analysis
        Given the eprime page is displayed
        When user analyses sentence To be or not to be - Hamlet's dilemma
        Then user learns sentence has 2 be-verbs, 1 possible be-verbs and total 9 words

    Scenario Outline: Eprime samples are correctly analyzed
        Given the eprime page is displayed
        When user analyses sentence <sentence>
        Then user learns sentence has <count_certain> be-verbs, <count_possible> possible be-verbs and total <count_total> words

        Examples:
        | sentence    | count_certain | count_possible | count_total |
        | was not     | 1             | 0              | 2           |
        | cat is hat  | 1             | 0              | 3           |


    
