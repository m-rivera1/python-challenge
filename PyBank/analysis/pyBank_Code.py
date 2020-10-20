# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:49:04 2020

@author: mike1
"""

import csv
import os

os.chdir("C:\\Users\\mike1\\Downloads")

budget_csv = "Budget_data.csv"


profit_loss = [] 
months_list = []

# Read in the CSV file
    
with open(budget_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
        
    for row in csvreader:
        profit_loss.append(int(row[1]))
        months_list.append(row[0])       

             




def print_analysis (profit_loss):
    
    
    total_months = len(profit_loss)
    monthly_total = sum(profit_loss)
    average = monthly_total/len(profit_loss)
    greatest_increase = max(profit_loss)
    greatest_decrease = min(profit_loss)
    
    #get index of greatest increase and decrease
    #then grab the date with same index number
    #from the months_list

    print("Financial Analysis")
    print("-------------------------")
    print(f' Total Months: {total_months}')  
    print(f' Total: ${monthly_total}')
    print(f' Average Change: ${average}')
    print(f' Greatest Increase in Profits:  ${greatest_increase}')
    print(f' Greatest Decrease in Profits:  ${greatest_decrease}')


 
   

print_analysis(profit_loss)
   
   

        
        