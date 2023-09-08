import os
import csv

#Provides the file relative path for budget data

budget_csv="Resources\\budget_data.csv"

#Determine the required variables

net_total=0

row_count=0

greatest_increase=0

greatest_increase_date=0

greatest_decrease=0

greatest_decrease_date=0

previous_net=0

changes=[]


#Open and Read the budget_data file

with open(budget_csv, 'r') as csv_file:
    
    csv_reader = csv.reader(csv_file)
    
    #Store the headers row

    header=next(csv_reader)
    
    #Reading the first row of the dataset

    first_row = next(csv_reader)

    row_count = row_count + 1

    previous_net = int( first_row[1] )

    net_total = net_total+previous_net
    
    #Determine the Total Months, Total Net Amount, Changes in Profit/Losses

    for row in csv_reader:
        
        row_count=row_count+1
        
        profit_loss=int(row[1])
        
        net_total = net_total + profit_loss
        
        net_change= int(row[1]) - previous_net
        
        previous_net = int(row[1])
        
        changes.append(net_change)
        
        date=row[0]
        
        
        #Determine the Greatest Increase & Date
        
        if net_change > greatest_increase:
          greatest_increase = net_change
          greatest_increase_date = date

        #Determine the Greatest Decrease & Date
        
        if net_change < greatest_decrease:
          greatest_decrease = net_change
          greatest_decrease_date = date

#Find the Average of Changes in Profit/Losses

average_change=round(sum(changes)/len(changes),2)

#Defines the Results Strings to Display in Terminal

Output_Text = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {row_count}\n"
f"Total: ${net_total}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
)

#Display the Results in Terminal

print(Output_Text)

#Export the Results in Output text file

text_file = "analysis\\Output.txt"

with open(text_file, 'w') as output_file:
   
   output_file.write(Output_Text)