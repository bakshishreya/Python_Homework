# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# # Module for 
# import statistics
# import numpy 

csvpath = os.path.join( 'Resources', 'election_data.csv')

# varriables
fsa = []
pl = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        #print(row[0])
        fsa.append(row[0])
        #pl.append(int(row[1]))

print(f"Total number of votes casted : {len(fsa)}")
