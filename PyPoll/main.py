
import os
import csv
from pathlib import Path
    
election_data = Path("python-challenge\PyPoll\Resources\election_data.csv")
    
with open(election_data, newline="", encoding="utf-8") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csvreader)
    
    # Lists to store data
    total_votes = 0
    candidate_list = []
    candidate_percent = []
    candidate_absolute = 0
        
    # iterate thru rows
    for row in csvreader:
            
    # read each column to get totals
        total_votes.append([0])
        candidate_list.append([2])
    
    total_votes = (len(total_votes))
    print(f"Total Votes: {total_votes}")
              
    # Pull candidates from listed summary table
    Khan = int(candidate_list.count("Khan"))
    Correy = int(candidate_list.count("Correy"))
    Li = int(candidate_list.count("Li"))
    # OTooley".strip(')
    # O'Tooley = int(strip(')(candidate_list.count("O'Tooley")))
    OTooley = int(candidate_list.count("OTooley"))
    
    # Pull Candidate vote percentage
    Khan_percent = ((Khan/total_votes)*100)
    Correy_percent = ((Correy/total_votes)*100)
    Li_percent = ((Li/total_votes)*100)
    OTooley_percent = ((OTooley/total_votes)*100)
    
    # Print name, vote percent, absolute count
    print(f"Khan: {Khan_percent}% ({Khan})")
    print(f"Correy: {Correy_percent}% ({Correy})")
    print(f"Li: {Li_percent}% ({Li})")
    print(f"OTooley: {OTooley_percent}% ({OTooley}")
    
    # define For Loop highest percentage of vote
    if OTooley > Li > Correy > Khan:
            Winner = "OTooley"
    elif Li > Correy > Khan > OTooley:
            Winner = "Li"
    elif Correy > Khan > OTooley > Li:
            Winner = "Correy"
    elif Khan > OTooley > Li > Correy:
            Winner = "Khan"
    print(f"Winner: {Winner}")
              
# print summary table:
print(f"Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print(f"Khan: {Khan_percent}% ({Khan})")
print(f"Correy: {Correy_percent}% ({Correy})")    
print(f"Li: {Li_percent}% ({Li})")
print(f"OTooley: {OTooley_percent}% ({OTooley})")
print("---------------------------")
print(f"Winner: {Winner}")
print("--------------------------")
    
# print to analysis file:
    
outgoing_electuibt_data = Path("python-challenge\PyPoll\analysis\analysis.txt")
    
with open('analysis.txt', 'w') as f:
    f.write('analysis')
