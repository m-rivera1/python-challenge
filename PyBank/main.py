# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:49:04 2020

@author: mike1
"""

import csv
import os

os.chdir("C:\\Users\\mike1\\Downloads")

budget_csv = "Budget_data.csv"

# establish empy dictionary
profit_loss = {} 


# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    # loop to add data to profit_loss dict    
    for row in csvreader:
        profit_loss.update({row[0]: int(row[1])})
        
  


#define function to calculate and print
def print_analysis (profit_loss):
    
    #calculations
    total_months = len(profit_loss.values())
    monthly_total = sum(profit_loss.values())
    average = monthly_total/len(profit_loss.values())
    greatest_increase = max(profit_loss.values())
    greatest_decrease = min(profit_loss.values())

    #loop to find the corresponding keys for the greatest
    #increase and decrease
    for key, value in profit_loss.items():
        if value == greatest_decrease:
           de_date = key
        if value == greatest_increase:
            in_date = key
    
        
    
 
    #print table
    print("              Financial Analysis")
    print("------------------------------------------------")
    print(f' Total Months:                 {total_months}')  
    print(f' Total:                        ${monthly_total}')
    print(f' Average Change:               ${round(average,2)}')
    print(f' Greatest Increase in Profits: {in_date} ${greatest_increase}')
    print(f' Greatest Decrease in Profits: {de_date} ${greatest_decrease}')

 
   
#call function to run analysis and print
print_analysis(profit_loss)