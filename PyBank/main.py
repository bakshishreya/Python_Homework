# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import numpy as np

#Path of CSV file
csvpath = os.path.join( 'Resources', 'budget_data.csv')

# varriables
fsa = []
pl = []
change=[]
monthly_profit_change =[]

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
  
    # Read each row of data after the header
    for row in csvreader:
        #print(row[0])
        fsa.append(row[0])
        pl.append(int(row[1]))


#net change
for i in range(len(pl)-1):
    # curr=pl[i]
    # futr=pl[i+1]
    # change=futr-curr

    monthly_profit_change.append(pl[i+1]-pl[i])
    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)

    max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 


    
print("Financial Analysis")
print("----------------------------")
print(f"Total number of months : {len(fsa)}")
# print amount of Profit/Losses over the entire period
print(f"The net total amount of Profit/Losses over the entire period:{sum(pl)}")
#print(f"Average Change: {(sum(change)/len(change))}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {fsa[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {fsa[max_decrease_month]} (${(str(max_decrease_value))})")


# # Output files
output_path = os.path.join( "Analysis","Analysis.txt")

with open(output_path,"w") as file:
    
# Write methods to print to Analysis_Summary 
     file.write("Financial Analysis""\n")
    
     file.write("----------------------------""\n")
 
     file.write(f"Total Months: {len(fsa)}""\n")
    
     file.write(f"Total: ${sum(pl)}""\n")
     
     file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}""\n")
   
     file.write(f"Greatest Increase in Profits: {fsa[max_increase_month]} (${(str(max_increase_value))})""\n")
    
     file.write(f"Greatest Decrease in Profits: {fsa[max_decrease_month]} (${(str(max_decrease_value))})""\n")



