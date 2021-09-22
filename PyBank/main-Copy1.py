Import os
Import csv
Import math
Import statistics

Budget_data = os.path.join('C:\Users\mdebo\DataClass\python-challenge\PyBank\Resources', 'Resources', 'budget_data.csv')

# Dictionary to store budget data
budget_dictionary = { 
    “date” : “Jan-2010”,
    “profit_Loss”: “867884”
}

# The total number of months included in the dataset
print(len(budget_dictionary))

# The net total amount of "Profit/Losses" over the entire period
def total(Profit_Loss):
    y = 0
    For x in profit_loss:
        y + x
    return y

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
Def average(profit_loss):
    i = 0
    for x in profit_loss:
        i +=j
    return y/len(profit_loss)

# The greatest increase in profits (date and amount) over the entire period
    f = max(profit_loss)

# The greatest decrease in profits (date and amount) over the entire period
    f = min(profit_loss)