# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initialize a vote counter
total_votes=0
#declare candidate list
candidate_options = []
#create candidate dictionary 
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file. add to the total vote count
# Print each row in the CSV file.
    for row in file_reader:
       # Add to the total vote count.
       total_votes += 1
    # Print the candidate name from each row.
       candidate_name = row[2]
       #add number of votes per candidate
       # If the candidate does not match any existing candidate...
       if candidate_name not in candidate_options:
           # Add it to the list of candidates.
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name]=0
           #Begin tracking vote counts and  #Add a vote to that candidate's counts
       candidate_votes[candidate_name] =candidate_votes[candidate_name]+ 1
#save to text file
with open(file_to_save, "w") as txt_file:
    f'Election Results\n------\nTotal Votes: 369,711\n------\n'
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)   
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}\n")
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

#     # print the candidate vote dictionary
#     print(candidate_votes)
#     # Print the candidate list.
#     print(candidate_options)
#     # Determine winning vote count and candidate
#     # 1. Determine if the votes are greater than the winning count.
#     if (votes > winning_count) and (vote_percentage > winning_percentage):
#         # 2. If true then set winning_count = votes and winning_percent =
#         # vote_percentage.
#         winning_count = votes
#         winning_percentage = vote_percentage
#         # 3. Set the winning_candidate equal to the candidate's name.
#         winning_candidate = candidate_name
#     #Your code should look like this:

#     # Determine the percentage of votes for each candidate by looping through the counts.
#     # Iterate through the candidate list.
#     for candidate_name in candidate_votes:
#         # Retrieve vote count of a candidate.
#         votes = candidate_votes[candidate_name]
#         # Calculate the percentage of votes.
#         vote_percentage = float(votes) / float(total_votes) * 100

#         #  To do: print out each candidate's name, vote count, and percentage of
#         # votes to the terminal.

#     # Determine winning vote count and candidate
#     # Determine if the votes is greater than the winning count.      # If true then set winning_count = votes and winning_percent =
# # vote_percentage.  # And, set the winning_candidate equal to the candidate's name.
#     if (votes > winning_count) and (vote_percentage > winning_percentage):
#         winning_count = votes
#         winning_percentage = vote_percentage   
#         winning_candidate = candidate_name
# #  To do: print out the winning candidate, vote count and percentage to
# #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# winning_candidate_summary = (
# f"-------------------------\n"
# f"Winner: {winning_candidate}\n"
# f"Winning Vote Count: {winning_count:,}\n"
# f"Winning Percentage: {winning_percentage:.1f}%\n"
# f"-------------------------\n")
# #print(winning_candidate_summary)
# candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# #  Save the candidate results to our text file.
# txt_file.write(candidate_results)
