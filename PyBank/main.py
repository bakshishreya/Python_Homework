# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# # Module for 
# import statistics
# import numpy 

csvpath = os.path.join( 'Resources', 'budget_data.csv')

fsa = []
pl = []

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

print(f"Total number of months : {len(fsa)}")

for i in range(len(pl)-1):
    curr=pl[i]
    futr=pl[i+1]
    change=futr-curr
    print(change)

print(pl)
print(f"The net total amount of Profit/Losses over the entire period:{sum(pl)}")
 
    
 
    
    # # The total number of months included in the dataset
    # with open(csvpath) as csvfile:
    # for row in csv.reader(csvfile):
    #     row = [int(val) for val in row]
    #     row.append(sum(row))
    #     new_rows.append(row)
        # # Loop through looking for the video
        # for row in csvreader:
        # if row[0] == Month:
        #     print(row[0] + " is rated " + row[1] + " with a user rating of " + row[5])
        #     found = True


 



    
    
