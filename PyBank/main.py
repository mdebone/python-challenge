import os
import csv
from pathlib import Path

budget_data = Path("python-challenge","PyBank","Resources","budget_data.csv") 

with open(budget_data, newline="", encoding='utf-8') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csvreader)

    # Lists to store data
    months = []
    month_count = 0
    profit = []
    total_to_date = 0
    avg_change = []
    
    
    # iterate thru rows
    for row in csvreader:
    
        # read each row to get total months
        month_count = month_count + 1 
        months.append([0])
        
        # total over the entire period
        total_to_date = total_to_date + int(row[1])

    # loop thru changes in profit loss column
    for i in range(1,len(profit)):
        avg_change.append(profit[i] - profit[i-1])
        mean_avg_change = sum(avg_change)/len(avg_change)
               
        # find max and min, and associated date
        max_avg_change = max(avg_change)

        min_avg_change = min(avg_change)

        max_month = str(months[avg_change.index(max_avg_change)])

        min_month = str(months[avg_change.index(min_avg_change)])

# print summary table:
print("Financial Analysis")
print("----------------------")
print(f"Total Months:  {month_count}")
print(f"Total: ${total_to_date}")
print(f"Average  Change: ${round(mean_avg_change, 2)}")
print(f"Greatest Increase in Profits: {max_month},${max_avg_change}")
print(f"Greatest Decrease in Profits: {min_month},${min_avg_change}")

# print to analysis file:

outgoing_budget_data = Path("python-challenge", "PyBank", "analysis.txt")

with open('analysis.txt', 'w') as f:
    f.write('analysis')
