import numpy as np

#Read input
with open('Day 6\input1.txt') as f:
    text = f.readlines()

#Save the ages of the input in a list where the first
#position is the number of fishes with 0 days until 
#produce a new one, the second number of fishes with
#1 days until produce a new one...
ages = list(map(int,text[0].split(",")))
ages = np.array(ages)
numAges = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in ages:
    numAges[i]+=1

#Simulate eache day one by one changing the list
maxDays = 256
days = 1
newChilds = 0
while(days <= maxDays):
    if numAges[0] > 0:
        newChilds = numAges[0]
        numAges[0] = 0
    for i in range(1,9):
        numAges[i-1] += numAges[i]
        numAges[i] = 0
    numAges[6] += newChilds
    numAges[8] += newChilds
    days += 1
    newChilds = 0
print(np.sum(numAges))

