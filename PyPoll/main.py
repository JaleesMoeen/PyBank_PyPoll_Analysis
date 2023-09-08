import os
import csv

#Provides the file relative path for budget data

election_csv="Resources\\election_data.csv"

#Determine the required variables

row_count=0

candidates_list=[]      #Store candidate names

candidate_votes={}      #Dictionary to store "candidate names" as 'key' against "votes" they receive as 'values'

percentage_votes={}     #Dictionary to store "candidate names" as 'key' against "percentage of votes received" as 'values'

winner_name= ""         

highest_percentage_of_votes = 0

#Open and Read the budget_data file

with open(election_csv, 'r') as csv_file:
    
    csv_reader = csv.reader(csv_file)

    #Store the headers row
    
    header = next(csv_reader)

    #Counting the rows and collecting unique candidate name

    for row in csv_reader:
        
        row_count = row_count+1
        
        candidate = str(row[2])
        
        if candidate not in candidates_list:
            candidates_list.append(candidate)

    #Calculating the number of votes each candidate received

        if candidate not in candidate_votes:
                candidate_votes[candidate] = 1
        else:
                candidate_votes[candidate] += 1

#For each candidate, find percentage of votes

percentage_votes = {}

for candidate,votes in candidate_votes.items():
                    
                    percentage = (votes/row_count)*100
                    
                    percentage_votes[candidate] = percentage

#Find winner name from the candidate names dictionary

                    for candidate, percentage in percentage_votes.items():
                        
                        if percentage>highest_percentage_of_votes:
                         
                         highest_percentage_of_votes = percentage
                         
                         winner_name = candidate


#Set Path for Output Text File
text_file = "analysis\\Output.txt"

with open(text_file, 'w') as output_file:

    #Defines the Election Results 
        
    Output_Text1 = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {row_count}\n"
    f"-------------------------\n"
    )
    
    #Display Election Results in Terminal
    
    print(Output_Text1)
    
    #Write the Elections Results to text file
    
    output_file.write(Output_Text1)


    #Defines List of Candidates Who Received Votes 
    
    for candidate in candidates_list:
        Output_Text2 = (f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidate_votes[candidate]})\n")
        print(Output_Text2)
        output_file.write(Output_Text2)


    Output_Text3 = (
    f"-------------------------\n"
    f"Winner: {winner_name}\n"
    f"-------------------------"
    )
    
    #Display Candidates List in Termial
    
    print(Output_Text3)

    #Write the Candiates List in Output Text File
    
    output_file.write(Output_Text3)