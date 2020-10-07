# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:24:54 2020

@author: VHowell
"""

import os 
import csv 

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',') 
    csv_header = next(csvreader) 
   # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header  
    totalvote = []  
    votekhan = []
    voteCorrey = []
    voteLi = []
    voteOT = []
    
    for row in csvreader:  
        ID = row[0] 
        totalvote.append(ID)  
        Total = len(totalvote) 
        
        
        if row[2] == "Khan"  :
            votekhan.append(row[0]) 
            
        if row[2] == "Correy" :
            voteCorrey.append(row[0])
            
        if row[2] == "Li" :
            voteLi.append(row[0])
            
        if row[2] == "O'Tooley" :
            voteOT.append(row[0])
        
    for i in range(0, len(totalvote)):  
            totalvote[i] = int(totalvote[i])    
        
        
bloop = sum(totalvote)  
 
plop = len(votekhan)   
hola = round((100*plop/Total),4) 

mia = len(voteCorrey)
daisy = round((100*mia/Total),4)  

dog = len(voteLi)
pets = round((100*dog/Total),4)  

doop = len(voteOT) 
pie = round((100*doop/Total),4)  

array = [pie, pets, daisy, hola]
winner = max(array)  

place = array.index(winner)  



if place ==0 :
    Win = "O'Tooley" 
    
if place ==1  :
    Win = "Li" 
    
if place == 2 :
    Win = "Correy" 
    
if place == 3 :
    Win = "Khan"
    
    
print("Election Results")
print("----------------------")
print(f"Total Votes: {Total} ")
print("----------------------")
print(f"Khan: ${winner}% ({plop})")    
print(f"Correy: ${daisy}%  ({mia})")     
print(f"Li: {pets}% ({dog})")      
print(f"O'Tooley': {pie}% ({doop})") 
print("----------------------")
print(f"Winner: {Win}")
print("----------------------")


with open("Analysis\exportresults.txt", "w") as f:

    print("Election Results", file = f)
    print("----------------------", file = f)
    print(f"Total Votes: {Total} ", file = f)
    print("----------------------", file = f)
    print(f"Khan: ${winner}% ({plop})", file = f)    
    print(f"Correy: ${daisy}%  ({mia})", file = f)     
    print(f"Li: {pets}% ({dog})", file = f)      
    print(f"O'Tooley': {pie}% ({doop})", file = f) 
    print("----------------------", file = f)
    print(f"Winner: {Win}", file = f)
    print("----------------------", file = f)
    



        