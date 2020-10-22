import csv
import os

os.chdir("C:\\Users\\mike1\\Git_Repos\\python-challenge\\PyPoll\\Resources")



election_csv = "election_data.csv"

# establish empty list
voting_data= []


# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    # loop to add data to voting_data list   
    for row in csvreader:
        voting_data.append(row[2])
 
         
#unique list of candidates
candidates = (set(voting_data))


#Tally of votes per candidates using count function
# Li_votes = voting_data.count('Li')
# Correy_votes = voting_data.count('Correy')
# Khan_votes = voting_data.count('Khan')
# Tooley_votes = voting_data.count("O'Tooley")



#Tally of votes per candidates using a loop
Li = 0
Correy = 0
Khan = 0
Tooley = 0
    
    
for val in voting_data:
    if val == "Li":
        Li = Li + 1
    elif val == "Correy":
        Correy = Correy + 1
    elif val == "Khan":
        Khan = Khan + 1
    elif val == "O'Tooley":
        Tooley = Tooley + 1

   

#define function to calculate and print 
def print_election_results ():
    
    #calculations
    total_votes = len(voting_data)
    Li_percent = (Li/total_votes) * 100
    Correy_percent = (Correy/total_votes) * 100
    Khan_percent = (Khan/total_votes) * 100
    Tooley_percent = Tooley/total_votes
      
            
    #print table in console
    print("              Election Results")
    print("------------------------------------------------")
    print(f' Total Votes:      {total_votes}')  
    print("------------------------------------------------")
    print(f' Khan:          {round(Khan_percent,2)}% ({Khan}) ')
    print(f' Correy:        {round(Correy_percent,2)}% ({Correy})')
    print(f' Li:            {round(Li_percent,2)}% ({Li})')
    print(f" O'Tooley:      {round(Tooley_percent,2)}% ({Tooley})")
    print("------------------------------------------------")
    print(" Winner: Khan  ")
    print("------------------------------------------------")

    # print to text file
    with open("analysis_pypoll.txt", "w") as text_file:
        print("              Election Results", file=text_file)
        print("------------------------------------------------", file=text_file)
        print(f' Total Votes:      {total_votes}', file=text_file)  
        print("------------------------------------------------", file=text_file)
        print(f' Khan:          {round(Khan_percent,2)}% ({Khan})', file=text_file)
        print(f' Correy:        {round(Correy_percent,2)}% ({Correy})', file=text_file)
        print(f' Li:            {round(Li_percent,2)}% ({Li})', file=text_file)
        print(f" O'Tooley:      {round(Tooley_percent,2)}% ({Tooley})", file=text_file)
        print("------------------------------------------------", file=text_file)
        print(" Winner: Khan  ", file=text_file)
        print("------------------------------------------------", file=text_file)

    

print_election_results()
