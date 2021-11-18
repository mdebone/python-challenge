import csv
from pathlib import Path


election_data = Path("PyPoll/Resources/election_data.csv")

# Lists to store data
vote_count = 0
votes = []
candidate = []
candidate_list = []
candidate_votes = {}
total_votes = 0
candidate_percent = []
candidate_absolute = 0
winner = ""
winner_count = 0
winner_percent = 0

 
with open(election_data, newline="", encoding="utf-8") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    #skip the header
    csv_header = next(csvreader)
    vote_count += 1
   
    # iterate thru rows
    for row in csvreader:
       
        # read each column to get totals
        candidate = row[2]

        # keep track of each counted vote
        vote_count = vote_count + 1

        # keep track of the candidates
        if candidate not in candidate_list:
                # add the candidate to the list
                candidate_list.append(candidate)
                # being tracking their votes from then on
                candidate_votes[candidate] = 0
                # Add a tally to that candidate's count
        candidate_votes[candidate] += 1

total_votes = vote_count
print(f"Total Votes: {total_votes}")

#all this below is dumb, so this is a new take ↓↓↓↓
for candidate in candidate_votes:
        # pull vote count and percentage of vote
        votes = candidate_votes[candidate]
        candidate_percent = int(votes)/int(total_votes) * 100
        candidate_result = (
                f"{candidate}: {candidate_percent:.1f}% ({votes:,})\n"
        )

        # print results and %
        print(candidate_result)

        # determine winner name, total, and percentage
        if(votes > winner_count) and (candidate_percent > winner_percent):
                winner = candidate
                winner_count = votes
                winner_percent = candidate_percent

# print the winner results to the terminal
election_analysis = (
f"Election Results\n"
f"---------------------------\n"
f"Total Votes: {total_votes:,}\n"
f"---------------------------\n"
f"Election Winner: {winner}\n"
f"Winner Votes Cast: {winner_count}\n"
f"Winner Percentage of Votes Cast: {winner_percent:.1f}%\n"
f"---------------------------\n"
)

print(election_analysis)

with open('PyPoll/analysis/election_analysis.txt', 'w') as f:
    f.write(election_analysis)

         
# # Pull candidates from listed summary table
# Khan = int(candidate_list.count("Khan"))
# Correy = int(candidate_list.count("Correy"))
# Li = int(candidate_list.count("Li"))
# #OTooley".strip(')
# #O'Tooley = int(strip(')(candidate_list.count("O'Tooley")))          
# OTooley = int(candidate_list.count("O'Tooley"))
   
# # Pull Candidate vote percentage
# Khan_percent = (Khan/total_votes)*100
# Correy_percent = (Correy/total_votes)*100
# Li_percent = (Li/total_votes)*100
# OTooley_percent = (OTooley/total_votes)*100
   
# # Print name, vote percent, absolute count
# print(f"Khan: {Khan_percent}% ({Khan})")
# print(f"Correy: {Correy_percent}% ({Correy})")
# print(f"Li: {Li_percent}% ({Li})")
# print(f"O'Tooley: {OTooley_percent}% ({OTooley})")
   
# # define For Loop highest percentage of vote
# if OTooley > Li > Correy > Khan:
#                 winner = "O'Tooley"
# elif Li > Correy > Khan > OTooley:
#                 winner = "Li"
# elif Correy > Khan > OTooley > Li:
#                 winner = "Correy"
# elif Khan > OTooley > Li > Correy:
#                 winner = "Khan"
# print(f"Winner: {winner}")
         
# print summary table:

# f"Khan: {Khan_percent}% ({Khan})\n"
# f"Correy: {Correy_percent}% ({Correy})\n"   
# f"Li: {Li_percent}% ({Li})\n"
# f"OTooley: {OTooley_percent}% ({OTooley})\n"
# "---------------------------\n"
# f"Winner: {winner}\n"
# "---------------------------\n")

# print(election_analysis)
 
# print to analysis file:
 
#outgoing_electuibt_data = Path("DataClass/python-challenge/PyPoll/analyysis/analysis.txt")
 
# with open('PyPoll/analysis/election_analysis.txt', 'w') as f:
#     f.write(election_analysis)