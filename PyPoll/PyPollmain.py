# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

# varriables
fsa = []
pl = []
myset=(pl)
candi_rec_vot=[]

with open(csvpath) as csvfile:
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
  # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

#1.The total number of votes cast
    for row in csvreader:
        #print(row[1])
        fsa.append(row[0])
        pl.append(row[2])

print(f"Total number of votes casted : {len(fsa)}")

#2.A complete list of candidates who received votes
for x in pl:
    if x not in candi_rec_vot:
       candi_rec_vot.append(x)
print("A complete list of candidates who received votes ")
print(candi_rec_vot)


#3.The percentage of votes each candidate won
# for candy in candy_list:
#     print(f'[{str(candy_list.index(candy))}] {candy}')


#4.The total number of votes each candidate won

