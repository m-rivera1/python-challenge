import csv
import os

os.chdir("C:\\Users\\mike1\\Downloads")

election_csv = "election_data2.csv"

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
 
        
print(voting_data)
        


#unique list of candidates
candidates = (set(voting_data))
print(candidates)


#Tally of votes per candidates using count function
Li_votes = voting_data.count('Li')
Correy_votes = voting_data.count('Correy')
Khan_votes = voting_data.count('Khan')
Tooley_votes = voting_data.count("O'Tooley")

print(Li_votes)
print(Correy_votes)
print(Khan_votes)
print(Tooley_votes)

#Tally of votese per candidates using a loop
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

print(Li)
print(Correy)
print(Khan)
print(Tooley)      

    

#************************************************
#need to calculate % votes per candidate


#***********************************************

#define function to calculate and print 
def print_election_results ():
    
    #calculations
    total_votes = len(voting_data)
    # monthly_total = sum(profit_loss.values())
    # average = monthly_total/len(profit_loss.values())
    # greatest_increase = max(profit_loss.values())
    # greatest_decrease = min(profit_loss.values())
    
    
    
        
    
 
    #print table in console
    print("              Election Results")
    print("------------------------------------------------")
    print(f' Total Votes:                 {total_votes}')  
    print("------------------------------------------------")
    print(f' Khan:                        ${monthly_total}')
    print(f' Average Change:               ${round(average,2)}')
    print(f' Greatest Increase in Profits: {in_date} ${greatest_increase}')
    print(f' Greatest Decrease in Profits: {de_date} ${greatest_decrease}')


    
     #print to text file
    with open("analysis.txt", "w") as text_file:
        print("              Financial Analysis", file=text_file)
        print("------------------------------------------------", file=text_file)
        print(f' Total Months:                 {total_months}', file=text_file)
        print(f' Total:                        ${monthly_total}', file=text_file)
        print(f' Average Change:               ${round(average,2)}', file=text_file)
        print(f' Greatest Increase in Profits: {in_date} ${greatest_increase}', file=text_file)
        print(f' Greatest Decrease in Profits: {de_date} ${greatest_decrease}', file=text_file)
        text_file.close()
        
        
#call function to run analysis and print
print_analysis(profit_loss)
