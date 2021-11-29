#Doc Analyzer

## Installations
Please run the following command to create a virtual environment.

`make install`

## Running tests
make test should run the test suite for the Doc Analyser application. Occasionally there is an issue
where a test will not always be shown to pass. However on subsequent runs the test will pass. Initial investigation
has lead me to believe this is a non deterministic issue with Spacy the app that powers all the analysis. 
I believe the algorithm sometimes does not correctly identify Nouns. Therefore on certain test runs we 
see a discrepancy.

`make test`

##  How to generate a report 

Place txt files that you wish to have analysed in the doc folder found in the root of this application
run the make generate command to create a csv that contains all the text analysis. This can be found in the
output folder.

`make generate`


