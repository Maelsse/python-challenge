#import csv module
import csv
import os

#declaring csv path
csvpath = os.path.join('election_data.csv') #/Users/myles/python-challenge/PyPoll/election_data.csv

with open (csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    #Lists & Variables
    votes=[]
    counties=[]
    candidates=[]
    candidatenames=[]
    v_count= 0
    loop_a = 0 #First loop for candidates
    linecount=0 

    for row in csvreader:
        voterid=row[0] # assign column 0 as voterid
        county=row[1] #assign column 1 as the county
        candidate=row[2] #assign column 2 as the candidates
        votes.append(voterid)
        counties.append(county)
        candidates.append(candidates)

v_count= len(votes)
print(v_count) 

candidatenames.append(candidates[0])

for loop_a in range(linecount-1):
    if candidates[loop_a+1] !=candidates[loop_a] and candidates[loop_a+1] not in candidates:
        candidates.append(candidates[0])
b=len(candidatenames)
print(b)