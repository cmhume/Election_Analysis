# Add dependencies
import csv
import os
# Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save file to path
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print header row
    headers = next(file_reader)
    print(headers)
# Print each row in CSV file

#1. Count total number of votes cast in election
#2. List all candidates who received votes in election
#3. Calculate % of votes each candidate received
#4. Count total number of votes each candidate received
#4. Determine the winner of the election based on popular vote


#Use open() with "w" mode to write election data in file
outfile = open(file_to_save,"w")
with open(file_to_save,"w") as txt_file:

#Write three counties to file
        txt_file.write("Counties in the Election\n")
        txt_file.write("-------------------------\n")
        txt_file.write("Arapahoe\nDenver\nJefferson\n")
        
        

#Close file

# Close file_to_load
