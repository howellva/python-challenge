# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:23:57 2020

@author: VHowell
"""


import os 
import csv 

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = '-') 
    csv_header = next(csvreader) 
   # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header  
    monthlist = []
    totalmonth = []  
    totalprofloss = []  
    
    
    
    for row in csvreader:  
        
        column1 = row[0] 
        totalmonth.append(column1)  
        
        Totalnumberofmonths = len(totalmonth) 
        
        if column1 not in monthlist :
            monthlist.append(column1)
 

with open(csvpath) as csvfile:
    csvreader2 = csv.reader(csvfile,delimiter = ',') 
    csv_header2 = next(csvreader2) 
    mark1 = []  
    mark2 = [] 
    answer = [] 
    bleep = []
    j = 1
    for row in csvreader2: 
       # print(row[1])
        column2 = row[1] 
        columnv = row[0]
        totalprofloss.append(column2)  
        bleep.append(columnv)
        
        for i in range(0, len(totalprofloss)):  
            totalprofloss[i] = int(totalprofloss[i])
            
    for i in range(0, len(totalprofloss)-1):    
        
        mark1.append(totalprofloss[i])
        mark2.append(totalprofloss[j])
        j = j+1
        difference = mark2[i]-mark1[i]  
        answer.append(difference) 
        average_change = sum(answer)/len(answer) 
        average_change = round(average_change,2)
        greatest_inc = max(answer)  
        greatest_dec = min(answer) 
        
hola = answer.index(greatest_inc)  
hello = answer.index(greatest_dec)  
date = bleep[hola+1]
date2 = bleep[hello+1]
            
Total = sum(totalprofloss)

print("Statistical Analysis")
print("----------------------")
print(f"Total Months: {Totalnumberofmonths} ")
print(f"Total: ${Total} ")    
print(f"Average Change: ${average_change} ")     
print(f"Greatest Increase in Profits: {date} (${greatest_inc})")      
print(f"Greatest Decrease in Profits: {date2} (${greatest_dec})") 



with open("Analysis\exportdata.txt", "w") as f:

    print("Statistical Analysis",file = f)
    print("----------------------",file = f)
    print(f"Total Months: {Totalnumberofmonths} ",file = f)
    print(f"Total: ${Total} ",file = f)    
    print(f"Average Change: ${average_change} ",file = f)     
    print(f"Greatest Increase in Profits: {date} (${greatest_inc})",file = f)      
    print(f"Greatest Decrease in Profits: {date2} (${greatest_dec})",file = f)               
       
     
        
     