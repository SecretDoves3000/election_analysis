# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

#load packages
import csv
import os

#assign variable for path of election result file 
file_to_load = os.path.join('resources','election_results.csv')

#create filename variable to a direct or indirect path to file
file_to_save = os.path.join('analysis','election_analysis.txt')

#1. Initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#open election results and read file
with open(file_to_load, 'r') as election_data:

    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)

    #read through the rows in the csv, each row is data for one ballot
    for row in file_reader:

        #Add a vote to the total count for each vote
        total_votes += 1

        #Get the candidates name from the ballot
        candidate_name = row[2]

        #If the name is not already in the list
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through counts

#Iterate through the candidate list.
for candidate_name in candidate_votes:

    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    #Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #Print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine the winning vote count and candidate
    #Deterime if the votes is greater than the winning count

    if (votes > winning_count) and (vote_percentage > winning_percentage):

        #if true than set winning_count = voetes and winning percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        #and, set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

#print the winning candidate, vote count and percentage
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)