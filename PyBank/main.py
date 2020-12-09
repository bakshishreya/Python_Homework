# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Module for 
import statistics
import numpy 

csvpath = os.path.join( 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #header = next(csvreader)
    #print(csvreader) 

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}"))
    
    # Read each row of data after the header
    for row in csvreader:
        print(row[0])
    
print()

fsa = []
    
fsa.append(row[0])
print(fsa)
 
    
 
    
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


 



    
    
