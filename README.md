#Doc Analyzer

## Installations
Please run the following command to create a virtual environment

`make install`

## Running tests
make test should run the test suite for the Doc Analyser application. Occasionally there is an issue
where a tests will not always be shown to pass on subsequent runs the tests will pass. Initially investigation
has lead me to believe this is a non deterministic issue with Spacy the app that powers all the analysis. 
I believe the algorithm sometimes does not correct identify Nouns. Therefore on certain test runs we 
see a discrepancy.

`make test`

##  How to generate a report 

Place txt files that you wish to have analysed in the doc folder found in the root of this application
run the make generate command to have a csv that contains all the text analysis of the docs found in the folder

`make generate`


