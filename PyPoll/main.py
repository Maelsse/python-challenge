# Total # of votes                              DONE
# List of candidates who got votes              DONE
# Percentage of votes for candidates            DONE
# Total votes each candidate                    DONE
# Winner of popular vote                
#import csv module
import csv
import os

#declaring csv path
csvpath = os.path.join('election_data.csv') #/Users/myles/python-challenge/PyPoll/election_data.csv

#Initializing Lists
votes=[] # List to store total number of votes in row [0]
counties=[] #List to store counties in row [1]
candidates=[] #List to store candidates in row [2]
candidatenames= []
cvotes = {}


#Initializing Variables
v_count = 0 #Initializing a variable to count votes
v_percentage = 0 #Initializing a variable to count percentages
winner = '' #election winner
c1_name = 'Charles Casper Stockham'
c2_name = 'Diana DeGette'
c3_name = 'Raymon Anthony Doane'
c1_count = 0
c2_count = 0
c3_count = 0
winning_count = 0

with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    for row in csvreader:
        voterid=row[0] # assign column 0 as voterid list
        county=row[1] #assign column 1 as the county list
        candidate=row[2] #assign column 2 as the candidates list
        if row[2] not in candidatenames:
            candidatenames.append(row[2])
        if str(candidate) == str(c1_name):
            c1_count += 1
        elif str(candidate) == str(c2_name):
            c2_count += 1
        elif str(candidate) == str(c3_name):
            c3_count += 1
        votes.append(voterid)
        counties.append(county)
        candidates.append(candidate)

v_count= len(votes) #Counting total number of votes cast
# print(v_count) 
c_names = len(candidatenames)
# print(
#     candidatenames,'\n',
#     v_count,'\n',
#     c_names,'\n',
#     c1_count,'\n',
#     c2_count,'\n',
#     c3_count
# )
c1_per = (c1_count / v_count) * 100
c2_per = (c2_count / v_count) * 100
c3_per = (c3_count / v_count) * 100

# print(
#         c1_percentage,'/n',
#         c2_percentage,'/n',
#         c3_percentage,'/n',
# )

voteTotalDict = {
    c1_name : c1_count, 
    c2_name : c2_count,
    c3_name : c3_count,
    }

winner = max(voteTotalDict, key=voteTotalDict.get)

# print (voteTotalDict.keys()[voteTotalDict.values().index(max(voteTotal))])
#Generating Outputs

analysis=f'\
    Election Results\n\
    -------------------------\n\
    Total Votes: {v_count} \n\
    -------------------------\n\
    {c1_name} : {round(c1_per,3)}% ({c1_count})\n\
    {c2_name} : {round(c2_per,3)}%({c2_count})\n\
    {c3_name} : {round(c3_per,3)}% ({c3_count})\n\
    -------------------------\n\
    Winner: {winner} \n\
    -------------------------'

print(analysis)
print(f'Congratulations {winner}!')

#Write into text file
pypollfile=open("pypoll.txt","w") #Open or create a new file 
pypollfile.writelines(analysis) #Print analysis
pypollfile.close() #Close file