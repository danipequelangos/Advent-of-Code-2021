import numpy as np

#Read input
with open('Day 6\input1.txt') as f:
    text = f.readlines()

#Save the ages of the input separetly
ages = list(map(int,text[0].split(",")))
ages = np.array(ages)

#Simulate the 80 days one by one
days = 1
while(days <= 80):
    childs = []
    for i in range(len(ages)):
        if ages[i]==0:
            ages[i] = 6
            childs.append(8)
        else:
            ages[i]-=1
    ages = np.append(ages, childs)
    days += 1
print(len(ages))

