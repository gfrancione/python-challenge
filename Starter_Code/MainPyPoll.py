# PyPoll Challenge
import os
import csv

# file to load and output
PyPollcsv =("PyPoll/Resources/election_data.csv")
file_to_output = ("analysis/election_analysis_1.txt")

#PyPollInstructions
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#Create the lists to store the data

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the csv file

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Count the votes
    for row in csvreader:
        # Count the total number of votes
        count = count + 1

        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # for check print(count)

        #Create a list to get unique candiate names
    for x in set(candidatelist):
        unique_candidate.append(x)

        # Y is the total number of votes per candidate
        y= candidatelist.count(x)
        vote_count.append(y)

        #Z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

    
    print("___________________________________")
    print("Election Results")
    print("-----------------------------------")          
    print("Total Votes :" + str(count))
    print("-----------------------------------")
    for i in range(len(unique_candidate)):
               print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
    print("-----------------------------------")
    print("winner " + winner)
    print("-----------------------------------")

    #Write a textfile to output


    with open('election_results.txt', 'w') as text:
          text.write("Elections Results\n")
          text.write("----------------------------")
          text.write("Total Vote: " + str(count) + "\n")
          text.write("-----------------------------")
          text.write ("Winner is: " + winner +"\n")
          text.write("-----------------------------")





        