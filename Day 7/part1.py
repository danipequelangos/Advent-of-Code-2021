import numpy as np

#Read input
with open('Day 7\input1.txt') as f:
    text = f.readlines()

#Save input in an array
positions = np.array(list(map(int,text[0].split(","))))

#From the minimum position to the maximum calculates the fuel 
#for all the positions to move to that position
fuelSums = np.array([])
for i in range(np.min(positions),np.max(positions)+1):
    fuelSum = np.sum(np.abs(positions-i))
    fuelSums = np.append(fuelSums,fuelSum)

print(np.argmin(fuelSums), int(np.min(fuelSums)))