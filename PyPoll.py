# Add dependencies
import csv
import os
# Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save file to path
file_to_save = os.path.join("analysis","election_analysis.txt")
# Initialize total vote counter
total_votes = 0
# Candidate Options
candidate_options = []
# Declare empty dictionary
candidate_votes = {}
# Track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read header row
    headers = next(file_reader)
    # Print each row in CSV file
    for row in file_reader:
        # Add total vote count
        total_votes += 1
        # Get candidate name from each row
        candidate_name = row[2]
        # Add if statement to only count candidate name once
        if candidate_name not in candidate_options:
                # Add candidate name to candidate list
                candidate_options.append(candidate_name)
                # Begin tracking candidate's vote count
                candidate_votes[candidate_name] = 0
        # Add votes to candidate count by increment
        candidate_votes[candidate_name] += 1 
        
for candidate_name in candidate_votes:
        #Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        #Calculate % of votes received out of total votes
        vote_percentage = float(votes)/float(total_votes)*100
        #Print each candidate name, votes received, and % of votes received to terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine winning vote count, winning percent and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
       # If true, set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
        # Set winning_candidate equal to candidate's name
                winning_candidate = candidate_name
# Print winning candidate's results in terminal
winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")
print(winning_candidate_summary)

 
# Print winning candidate's name, vote count and vote percentage to terminal

#print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#1. Count total number of votes cast in election
#2. List all candidates who received votes in election
#3. Calculate % of votes each candidate received
#4. Count total number of votes each candidate received
#4. Determine the winner of the election based on popular vote


#Use open() with "w" mode to write election data in file
#outfile = open(file_to_save,"w")
#with open(file_to_save,"w") as txt_file:

#Write three counties to file
        #txt_file.write("Counties in the Election\n")
        #txt_file.write("-------------------------\n")
        #txt_file.write("Arapahoe\nDenver\nJefferson\n")
        
        

#Close file

# Close file_to_load
