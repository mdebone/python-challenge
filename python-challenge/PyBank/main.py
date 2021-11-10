import os
import csv

budget_data = os.path.join('PyBank','Resources','budget_data.csv')

 # Lists to store data
months = []
month_count = 0
profit_losses = []
total_to_date = 0
running_total = 0
mean_avg_change = 0
max_avg_change = 0
min_avg_change = 0
max_month = 0
min_month = 0

# open the budget data csv
with open(budget_data, newline="", encoding='utf-8') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    #skip the header
    csv_header = next(csvreader)
    # read each row to get total months
    row = next(csvreader)
    month_count += 1
    total_to_date += int(row[1])
    running_total = int(row[1])

    # total over the entire period
    # iterate thru rows
    for row in csvreader:

        # get month from first column
        months.append(row[0])

        # get profit/losses as an integer from second column
        mean_avg_change = int(row[1]) -running_total
        profit_losses.append(mean_avg_change)
        running_total = int(row[1])

        # keep tack of month number
        month_count += 1

        # total net amount of the profit/losses column
        total_to_date = total_to_date + int(row[1])
    
    # greatest mothly increase in profits
    max_avg_change = max(profit_losses)
    max_avg_index = profit_losses.index(max_avg_change)
    max_month = months[max_avg_index]

    # worst monthly change in profits
    min_avg_change = min(profit_losses)
    min_avg_index = profit_losses.index(min_avg_change)
    min_month = months[min_avg_index]

    # average change in profit losses in a month to month basis
    mean_avg_change = sum(profit_losses)/len(profit_losses)


# print summary table:
print("Financial Analysis")
print("----------------------")
print(f"Total Months:  {month_count}")
print(f"Total: ${total_to_date}")
print(f"Average  Change: ${round(mean_avg_change, 2)}")
print(f"Greatest Increase in Profits: {max_month},${max_avg_change}")
print(f"Greatest Decrease in Profits: {min_month},${min_avg_change}")

# print to analysis file:

outgoing_budget_data = os.path("python-challenge", "PyBank", "analysis.txt")

with open('analysis.txt', 'w') as f:
    f.write('analysis')