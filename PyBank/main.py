#import csv module 
import csv
import os 

#declaring csv path
csvpath = os.path.join('budget_data.csv') #/Users/myles/python-challenge/PyBank/budget_data.csv

with open (csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    #Variables
    months=[]
    outcomes=[] #Profits/Losses

    # Conditions
    total= 0
    m_count=0
    m_change=0
    loop1= 0
    loop2= 0
    change=0
    incr=0
    decr=0
    cline1=0
    cline2=0


    # Reading the rows
    for row in csvreader:
        month=row[0] #First column is the month
        outcome=row[1] #Second column is pro/loss
        months.append(month) #line to list months
        outcomes.append(outcome)  #line to list outcomes
    
    m_count = len(months) #counting the total number of months 
    print(m_count)

    # BEGINNING DATA ANALYSIS

# This loop is to figure out total outcomes (Pro/Losses)

for loop1 in range(m_count):
    total=total+int(outcomes[loop1])
print(total)

# Calculating the changes per month

#for loop2 in range(m_count-1): 
   
    #change=change+(float(outcomes[loop2+1])-float(outcomes[loop2]))
    #print(change)
    #print(change/(m_count-1))
#Calculating monthly changes
    #incr=(float(outcomes[loop2+1])-float(outcomes[loop2]))
    #if m_change>incr: #Greatest increase
        #incr=m_change
        #cline1=loop2
   # else:
       # incr=incr
#print(incr)
#print(months[cline1+1])
  #  if m_change<decr:
   #     decr=m_change
   #     cline2=loop2
   # else:
    #    decr=decr

#print(decr)
#print(months[cline2+1])

#Generating Outputs

analysis=f'\
    Financial Analysis\n\
    Total Months: {m_count}\n\
    Total: {total}\n\
    Average Change: {change}\n\
    Greatest Increase in Profits: {incr}\n\
    Greatest Decrease in Profits: {decr}'

# print(analysis)

#Write into text file
# pybankfile=open("pybank.txt","w") #Open or create a new file 
# pybankfile.writelines(analysis) #Print analysis
# pybankfile.close() #Close file