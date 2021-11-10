import os
import csv
from pathlib import Path

budget_data = Path("PyBank","Resources","budget_data.csv")

with open(budget_data, newline="", encoding='utf-8') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csvreader)

    # Lists to store data
    month = 0
    total_to_date = 0
    profit = []
    net_total = []
    av_change = []
   
    # iterate thru rows
    for row in csvreader:
    
    
        # read each row to get total months
        month = 0
        if month > 0:
            print(row)
        month+=1
    
        # total over the entire period
        total_to_date = total_to_date + int(row[1])

        #profits.append(float(row[1])) ******

    # loop thru changes in profit loss column
    for i in range(1,len(profit)):
        net_total.append(profit[i] - profit[i-1])
        
        av_change = sum(net_total)/len(net_total)

    # find max and min, and associated date
    max_av_change = max(av_change)

    min_av_change = min(av_change)

    max_av_month = net_total.index(max(net_total))

    min_av_month = net_total.index(min(net_total))

# print summary table:
print("Financial Analysis")
print("----------------------")
print(f"Total Months:  {month}")
print(f"Total: $ {total_to_date}")
print(f"Average  Change: $ {av_change}")
print(f"Greatest Increase in Profits: ${max_av_month}{max_av_change}")
print(f"Greatest Decrease in Profits: ${min_av_month}{min_av_change}")

# print to analysis file:

outgoing_budget_data = Path("python-challenge", "PyBank", "analysis.txt")

with open('analysis.txt', 'w') as f:
    f.write('analysis')