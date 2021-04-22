import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

votes = 0

Candidates = []
vote_count = {}

winner = ""
winning_vote_count = 0

with open(file_to_load) as data:
    reader = csv.DictReader(data)
    
    for row in reader:
        print(". ", end=""),
        
        votes = votes + 1
        
        Candidates_name = row["Candidate"]
        
        if Candidates_name not in Candidates:
            
            Candidates.append(Candidates_name)
            
            vote_count[Candidates_name] = 0
            
        vote_count[Candidates_name] = vote_count[Candidates_name] + 1

        with open(file_to_output, "w"0 as txt_file:
    results = (
        f"\n\nResults\n"
        f"Total Votes: {votes}\n")
          
    print(election_results, end="")
    
    txt_file.write(election_results)
          
    for canidate in vote_count:
          
          votes = vote_votes

    