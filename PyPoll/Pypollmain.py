import os
import csv
poll_csv=os.path.join("Resources", "election_data.csv")
#make a dictionary
num_votes=[]
candidate=[]
unique_candidate=[]
percent_votes=[]
total_candidate=[]
winner=[]
num_votes=0


# print for loop to calculate percentages in for loop if in for loop as well
with open(poll_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header= next(csvreader)
    next_row=next(csvreader)
    num_votes+=1
    for row in csvreader:
        num_votes+=1
        candidate=row[2]
        if candidate in unique_candidate:
            candidate_list= unique_candidate.index(candidate)
            total_candidate[candidate_list]=total_candidate[candidate_list]+1
        else:
            unique_candidate.append(candidate)
            total_candidate.append(1)   
    all_votes=total_candidate[0]
    vote_index= 0 
    percentages=[]
    for count in range(len(unique_candidate)):
        percent_votes=total_candidate[count]/num_votes*100
        percentages.append(percent_votes)
        if total_candidate[count]>all_votes:
            all_votes=total_candidate[count]
            vote_index=count
            winner= unique_candidate[vote_index]

print(num_votes)
print(unique_candidate)  
print(total_candidate)
print(percentages)
print(winner)

print(f'Election results')
print(f'----------------------------')
print(f"Total Votes: {num_votes}")
print(f'----------------------------')
for count in range(len(unique_candidate)):
    print(f"{unique_candidate[count]}: {round(percentages[count], 2)}% ({total_candidate[count]})")
print(f'----------------------------')    
print(f'Winner:{winner}')
print(f'----------------------------') 

output_path=os.path.join("Analysis", "Analysis.txt")

with open(output_path, 'w') as writer:
    
    writer.writelines(f'Election results')
    writer.writelines("\n")
    writer.writelines(f'----------------------------')
    writer.writelines("\n")
    writer.writelines(f"Total Votes: {num_votes}")
    writer.writelines("\n")
    writer.writelines(f'----------------------------')
    writer.writelines("\n")
    for count in range(len(unique_candidate)):
        writer.writelines(f"{unique_candidate[count]}: {round(percentages[count], 2)}% ({total_candidate[count]})")
    writer.writelines("\n")
    writer.writelines(f'----------------------------')  
    writer.writelines("\n")
    writer.writelines(f'Winner:{winner}')
    writer.writelines("\n")
    writer.writelines(f'----------------------------')