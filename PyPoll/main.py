import csv
import os

os.chdir("C:\\Users\\mike1\\Downloads")

election_csv = "election_data2.csv"

# establish empy dictionary
voting_data= []


# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    # loop to add data to voting_data dict    
    for row in csvreader:
        voting_data.append(row[2])
 
        
print(voting_data)
        
# # pulled votes for all candidates into new list        
# candidate_votes = []
# for val in voting_data.values(): 
#     if val in voting_data: 
#         continue 
#     else:
#         candidate_votes.append(val) 
      

#unique list of candidates
candidates = (set(voting_data))
print(candidates)



Li_votes = voting_data.count('Li')
Correy_votes = voting_data.count('Correy')
Khan_votes = voting_data.count('Khan')
Tooley_votes = voting_data.count("O'Tooley")

print(Li_votes)
print(Correy_votes)
print(Khan_votes)
print(Tooley_votes)

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
#print(x)

# i = 1
# for val in candidates:
#     if val in candidate_votes:
#          for val in ccandidate_i = candidate_votes.count(val)

candidate_tally = {}
for val in candidates:
    i = 0
    if val in candidate_votes:
        counter = i + 1
    else:
        candidate_tally.update(val: counter)
        counter = 0
else:
    continue
        
        
        continue
    
print(candidate_tally)
    
#define function to calculate and print 
def print_election_results ():
    
    #calculations
    # total_votes = len(voting_data.values())
    # monthly_total = sum(profit_loss.values())
    # average = monthly_total/len(profit_loss.values())
    # greatest_increase = max(profit_loss.values())
    # greatest_decrease = min(profit_loss.values())
    
    candidate_list = []
    for val in voting_data.values(): 
        if val in voting_data: 
            continue 
        else:
           candidate_list.append(val) 
           
    print(candidate_list)


    #loop to find the corresponding keys for the greatest
    #increase and decrease
    for key, value in profit_loss.items():
        if value == greatest_decrease:
           de_date = key
        if value == greatest_increase:
            in_date = key
    
        
    
 
    #print table in console
    print("              Financial Analysis")
    print("------------------------------------------------")
    print(f' Total Months:                 {total_months}')  
    print(f' Total:                        ${monthly_total}')
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
