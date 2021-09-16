# import os
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# import math

# allows reading of CSV file
import csv

from pathlib import Path
budget_csv = Path("python-challenge","PyBank","Resources","budget_data.csv")
#budget_csv = "python-challenge","PyBank","Resources","budget_data.csv"
# get the filename
# print(Path(csvpath).name)

with open("budget_data.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        print(row['date'], row['profit_loss'])

    # Read the header row first
    # csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each for of data after the header
   # for row in csvreader:
   #     print(row)

budget = {}

budget = dict()

# Dictionary to store budget data
budget = { 
	"date": "Jan-2010",
	"profit_loss": 867884
}

# The total number of months included in the dataset
print(len(budget["date"]))

# The net total amount of "Profit/Losses" over the entire period
#def total(budget['profit_loss']))
    # y = 0
	    # for x in profit_losses:
		    # y +=x
	   # return y
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#def average(budget([profit_loss])):
#    i = 0
#    for x in profit_loss:
#	    i += x
#    return x/len(profit_loss)

# The greatest increase in profits (date and amount) over the entire period
# k = max(profit_loss)

# The greatest decrease in profits (date and amount) over the entire period
# f = min(profit_loss)







