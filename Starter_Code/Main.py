#Py Bank Challenge Module#3
import csv
import os

from panel import Row


#Load the CSV File into a pandas dataframe
PyBankcsv = 'PyBank/Resources/budget_data.csv'
PyPollcsv = 'PyPoll/Resources/election_data.csv'

test="./"


# PyBank Instructions
#       1.	The total number of months included in the dataset
#       2.	The total net amount of "Profit/Losses" over the entire period
#       3.	The average change in "Profit/Losses" between months over the entire period
#       4.	The greatest increase in profits (date and amount) over the entire period
#       5.	The greatest decrease in losses (date and amount) over the entire period


#List to record the data
profit =[]
monthly_changes = []
date = []

#Initialize the variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0


# Read the csv and convert it into a list of dictionaries
# Open the CSV using the set path PyBankcsv

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Financial_Analysis
    #Count the total number of months
    for row in csvreader:
        count = count + 1
       

        #Need date when collecting the greatest increase and decrease in profits
        date.append(row[0])

        #Append the profit information and calculate the total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        print (total_profit)

        #Calculate the average change in profits from month to month.
        final_profit = int(row[1])
        
        #Calculate the average change in profits
        monthly_change_profits = final_profit - initial_profit

        #Store the monthly changes in a list
        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        #Calculate the average change in profits
        average_change_profits = (total_change_profits/count)

        #Calculate the greatest and increase and decreaste in profits and report the dates
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

        print("----------------------------------------------")
        print("Financial Analysis")
        print("----------------------------------------------")
        print("Total Months: " + str(total_profit))
        print("Total Profits:" + str(int(average_change_profits)))
        print("Average Change: " + "$" + str(int(average_change_profits)))
        print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
        print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
        print("----------------------------------------------------------")

    with open('Financial_analyst.txt', 'w') as text:
        text.write("_____________________________________________")
        text.write("  Financial Analysis"+ "\n")
        text.write("----------------------------------------------------------\n\n")
        text.write("    Total Months: " + str(count) + "\n")
        text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
        text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
        text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
        text.write("----------------------------------------------------------\n")


