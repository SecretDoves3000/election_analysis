# Election Analysis

## Project Overview
We were tasked with tallying votes and evaluating results from a Colorado election. Our steps were:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.38.1

## Vote Breakdown by Candidate
The analysis if the election shows that:
- There were 369,711 total votes cast
- The Candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The ballot totals were:
  - Charles Casper Stockham recieved 85,213 votes for 23.0% of the total ballots.
  - Diana DeGette recieved 272,892 votes for 73.8% of the total ballots.
  - Raymon Anthony Doane recieved 11,606 votes for 3.1% of the total ballots.
- The winner of the election was:
  - Diana DeGette with 272,892 votes and 73.8% of the total ballots.

##Audit Challenge Overview
We were tasked with adding functionality to look at the voter turnout in each county and show the percentage of votes cast from each county

## Vote Breakdown by County
- Of the 369,711 total votes:
  - There were 38,855 votes cast in Jefferson for 10.5% of the vote.
  - There were 306,055 votes cast in Denver for 82.8% of the vote.
  - There were 24,801 votes cast in Arapahoe for 6.7% of the vote.
- Denver had the largest number of votes at 306,055 votes.

## Election-Audit Summary
The PyPoll script developed can be used with minor modifications to tally votes in any election. To do so, the script should be placed in a folder with the ballot data stored as a csv. The code on lines 8-11 should be adjusted to reflect the name and path of the files in question:
'''
'# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
'''
Some sections of the code need also be adjusted for different structures of ballot data. This will require investigating the structure of the ballot data csv. In particular the code on lines 46-50 needs to be adjusted so the index of the relevant data  
