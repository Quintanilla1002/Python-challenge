import os
import csv

budget_csv=os.path.join("Resources", "budget_data.csv")
months= []
net_total=[]
average_change=[]
greatest_increase=[]
greatest_decrease=[]

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)
    num_months= 0
    for row in open(budget_csv):
        next(csvreader, None)
        num_months+=1
        print(num_months)

