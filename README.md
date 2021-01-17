# Election-analysis



## Overview of Project

The overall goal of this project is to analyze election data from Colorado and determine the winner of the congressional election based on who received the highest percentage of votes. 

1. Calculate the total number of votes cast.
2. Get a complete list of candiates who received votes.
3. Calculate the total number of votes each candidate received
4. Calcualte the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote. 
6. Calculate the number of votes from each county and the county with the highest turnout. 


### Resources
-Data Source: election_results.csv
-Software: Python 3.7.6 (v3.7.6:43364a7ae0, Dec 18 2019, 14:18:50) 


### Purpose

To analyze election data and determine the winner. 

## Election Audit Results
The analysis of the election shows that: 
There were 369,711 votes cast in the election. 
There were three counties: their names and the number of votes from each county were: 
County Votes:
1. Jefferson: 10.5% (38,855)
2. Denver: 82.8% (306,055)
3. Arapahoe: 6.7% (24,801)

The highest turnout was from Denver

There were three candidates. Their names and the number of votes each received were:   
1. Charles Casper Stockham: 23.0% (85,213)
2. Diana DeGette: 73.8% (272,892)
3. Raymon Anthony Doane: 3.1% (11,606)

The winner of the election was Diana DeGette. She received the highest number of votes (272,892), with a winning percentage of 73.8%.
 

## Election-Audit Summary
The script provided for this analysis can be used in any election. If the data are organized differently then the index will need to be changed in the code e.g. 
     # Get the candidate name from each row.
        candidate_name = row[2]; the number two here wil need to changed to the index where candidate name exists in that particular dataset 
     # change the path for file to load and file to save depending on the folder structure and where the file is saved
        


