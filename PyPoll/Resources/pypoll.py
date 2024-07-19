
# Import Dependencies (modules)
import csv, os


# Create file to load and file to output the results 
# Use os.path.join() to return path components as a single string
    #load 
        #directory = ".",
        # filename = "election_data.csv"
    #output
        #directory = "."
        # filename = "election_analysis.txt"

file_to_load=os.path.join(".","election_data.csv")
file_to_output=os.path.join(".","election_analysis.txt")


# Set variables
    # Counter for total votes
total_votes=0

    # Winning candidate and Count Tracker 
winning_candidate=""
winning_count=0

        #dictionary
candidate_votes={}
        #list
candidate_options=[]



# Open & read election data using csv
with open(file_to_load) as election_data:

    reader=csv.reader(election_data)

    header=next(reader)
    

    for row in reader:
        # Count total votes by incrementing +1 
        total_votes=total_votes+1
        
        # Extract candidate name for each row
        candidate_name=row[2]
        
        # Adds the names of any new candidates to the candidate options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)


        # Use dictionary to track votes for each candidate
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
        



with open(file_to_output,"w") as txt_file:
   
    election_results=(
        f"Election Results\n"
        f"--------------------------------\n"
        f"Total Votes:  {total_votes}\n"
        f"--------------------------------\n"
    
    )

    print(election_results,end="")

    txt_file.write(election_results)

    # calculates percentage of votes for each candidate 
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]

        vote_percentage=float(votes)/float(total_votes)*100

        # calculate winning candidate based on great number of votes
        if(votes>winning_count):
            winning_count=votes
            winning_candidate=candidate

        voter_output = f"{candidate}:{vote_percentage:.3f}% ({votes})\n"
        
       
        print(voter_output,end="")

        txt_file.write(voter_output)

    winning_candidate_name=(
        f"--------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------------\n"
    )
    print (winning_candidate_name)
    txt_file.write(winning_candidate_name)

