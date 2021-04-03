# Election Analysis


## Project Overview


Given the data set, election_results.csv, complete the following tasks:


1) Calculate the total number of votes cast in the election

2) Get a complete list of candidates who received votes in the election

3) Calculate the total number of votes each candidate received in the election

4) Calculate the percent of votes each candidate won

5) Determine the winner of the election based on popular vote

6) Calculate voter turnout for each county

7) Calculate the percentage of votes from each county out of the total votes cast in the election

8) Determine the county with the highest voter turnout


## Resources


Data Source: election_results.csv


Starter code: PyPoll_Challenge_starter_code.py

Software: Python 3.6.7, Visual Studio Code version 1.54.3


## Election-Audit Results: 

The results from the analysis of this election are:


* There was a total of 369,711 votes cast in the election





* The number of votes and percentage of total votes for each County in the voting precinct were:
  
  
  * Arapahoe County: 6.7% of total votes (24,801 votes)
  * Denver County: 82.8% of total votes (306,055 votes)
  * Jefferson County: 10.5% of total votes (38,855 votes)


* The county with the largest voter turnout was:


  * Denver County 


* The number of votes and percentage of total votes received by each candidate was:


  * Diana Degette: 73.8% of votes (272,892 votes)
  * Raymon Anthony Doane: 3.1% of votes (11,066 votes)
  * Charles Casper Stockham: 23.0% of votes (85,213 votes)


* The winner of this election by popular vote was:


  * Diana Degette: 73.8% of the total vote count (272,892 votes)


## Election Audit Summary


The code used in this election-audit can be easily modified for future elections.  The path to the data file with any election's results can be placed in the file_to_load variable.  The code will read the requested file and create a list of candidates and counties present in the data, track votes for each candidate, the number of votes in each county, determine the winning candidate, the county with the largest voter turnout, and print the analysis to the election_analysis.txt file.  If needed, a different text file could also be used to write the results to by changeing the file_to_save variable with the path to the desired .txt file.  The index numbers for the columns with the data for candidate_name and county_name can be changed to correspond with their location in the new file_to_load by changing the number inside the square brackets after row, when the candidate_name and county_name are first assigned. With these actions, changing file_to_load, file_to_save and updating column index numbers, the results for any election can be easily tabulated and printed in the command line and a separate text file.
