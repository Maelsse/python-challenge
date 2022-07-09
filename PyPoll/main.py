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
candidate1_count = 0
candidate2_count = 0
candidate3_count = 0
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
            candidate1_count += 1
        elif str(candidate) == str(c2_name):
            candidate2_count += 1
        elif str(candidate) == str(c3_name):
            candidate3_count += 1
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
#     candidate1_count,'\n',
#     candidate2_count,'\n',
#     candidate3_count
# )
candidate1_percentage = (candidate1_count / v_count) * 100
candidate2_percentage = (candidate2_count / v_count) * 100
candidate3_percentage = (candidate3_count / v_count) * 100

# print(
#         candidate1_percentage,'/n',
#         candidate2_percentage,'/n',
#         candidate3_percentage,'/n',
# )

voteTotalDict = {
    c1_name : candidate1_count, 
    c2_name : candidate2_count,
    c3_name : candidate3_count,
    }

winner = max(voteTotalDict, key=voteTotalDict.get)

# print (voteTotalDict.keys()[voteTotalDict.values().index(max(voteTotal))])
#Generating Outputs

analysis=f'\
    Election Results\n\
    -------------------------\n\
    Total Votes: {v_count} \n\
    -------------------------\n\
    {c1_name} : {round(candidate1_percentage,3)}% ({candidate1_count})\n\
    {c2_name} : {round(candidate2_percentage,3)}%({candidate2_count})\n\
    {c3_name} : {round(candidate3_percentage,3)}% ({candidate3_count})\n\
    -------------------------\n\
    Winner: {winner} \n\
    -------------------------'

print(analysis)
print(f'Congratulations {winner}!')

#Write into text file
pypollfile=open("pypoll.txt","w") #Open or create a new file 
pypollfile.writelines(analysis) #Print analysis
pypollfile.close() #Close file