import os
import csv

budget_csv=os.path.join("Resources", "budget_data.csv")
months= []
net_total=[]
average_change=[]
greatest_increase=["", 0]
greatest_decrease=["", 1000000]

num_months=0
profit_losses=0
change=0
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    next_row=next(csvreader)
    num_months+=1
    profit_losses=profit_losses+int(next_row[1])
    previous_row=int(next_row[1])
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        #num_months=0
        print(row)
        #row in open(budget_csv):
        num_months+=1
        profit_losses=profit_losses+int(row[1])
        change=int(row[1])-previous_row
        previous_row=int(row[1])
        average_change.append(change)
        if change > greatest_increase[1]:
            greatest_increase[1]=change    
            greatest_increase[0]=row[0]
        if change < greatest_decrease[1]:
            greatest_decrease[1]=change
            greatest_decrease[0]=row[0]
print(num_months)
print(profit_losses)
average=sum(average_change)/len(average_change)
avg=round(average, 2)
print(avg)
print(greatest_increase)
print(greatest_decrease)
print(f'Financial Analysis')
print(f'----------------------------')
print(f"Total Months: {num_months}")
print(f"Total: ${profit_losses}")
print(f"Average  Change: ${avg}")
print(f"Greatest Increase in Profits: {greatest_increase[0]}, (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})")

text_path=os.path.join("..", "Analysis", "Analysis.txt")

with open(text_path, 'w') as file:
    file.write(f'Financial Analysis')
    file.write(f'----------------------------')
    file.write(f"Total Months: {num_months}")
    file.write(f"Total: ${profit_losses}")
    file.write(f"Average  Change: ${avg}")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]}, (${greatest_increase[1]})")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})")
    file.close