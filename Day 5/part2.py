import numpy as np

#Read input
with open('Day 5\input1.txt') as f:
    text = f.readlines()

#Save input as different lines 
lines = []
for i in text:
    line = i.split(" -> ")
    lines.append([list(map(int,line[0].split(","))),list(map(int,line[1].split(",")))])

#Make de diagram    
max = np.max(lines)
diagram = np.zeros((max+1,max+1))

#Represent the lines in the diagram
for line in lines:
    #if X equals
    if line[0][0] == line[1][0]:
        if line[0][1] > line[1][1]:
            yMax = line[0][1]
            yMin = line[1][1]
        else:
            yMax = line[1][1]
            yMin = line[0][1]
        x = line[0][0]
        for y in range(yMin,yMax+1):
            diagram[y,x]+=1
    #if Y equals
    elif line[0][1] == line[1][1]:
        if line[0][0] > line[1][0]:
            xMax = line[0][0]
            xMin = line[1][0]
        else:
            xMax = line[1][0]
            xMin = line[0][0]
        y = line[0][1]
        for x in range(xMin,xMax+1):
            diagram[y,x]+=1
    #Diagonal lines
    else:
        if line[0][1] > line[1][1]:
            directionY = -1
        else:
            directionY = 1

        if line[0][0] > line[1][0]:
            directionX = -1
        else:
            directionX = 1
        xRange = range(line[0][0],line[1][0]+directionX,directionX)
        yRange = range(line[0][1],line[1][1]+directionY,directionY)
        for i in range(len(xRange)):
            diagram[yRange[i],xRange[i]]+=1

print((diagram >= 2.0).sum())



