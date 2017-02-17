# journal-stats
For comparative analysis of academic journal publication data

Currently in development.  
  
### Program description ###
This program will go to The Astrophysical Journal website and retrieve the 'Received' and 'Accepted' dates for a sample of at least 500 articles, saving them into a spreadsheet.

Inputs: none  
Outputs: .csv file (open in Excel)

### Technical details ###

Assumptions:  
* There are at least 30 articles per issue
* There are 2 issues per volume
* There are 18 volumes per year (1.5 per month, averaged)

The program will attempt to load the URLs of the first 30 articles in issue 1 of a defined volume. It will retrieve the dates for as many of these as possible, before doing the same for issue 1 of the previous volume, and then issue 1 of the volume before that, etc.  

The program will loop through the latest 18 volumes in this manner, corresponding to the previous year, to return the dates for a sample of at least 500 articles (URLs on the ApJ website are not entirely consistent, so the date retrieval may fail for some articles).

For at least the last 5 years (2012 - 2016 inclusive), there have been 18 volumes  of ApJ per year, each with 2 issues. The program currently takes Volume 834 (Number 1, 1 January 2017) as a benchmark, and assumes that this pattern will continue. 



TO ADD: ApjL description, Quickstart guide, Troubleshooting
