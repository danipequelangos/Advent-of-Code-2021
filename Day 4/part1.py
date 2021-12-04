#Check if table wins
def checkWin(table):
    win = False
    #Check by row
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] != "X":
                win = False
                break
            else:
                win = True
        if win:
            return win

    #Check by column
    for i in range(len(table[0])):
        for j in range(len(table)):
            if table[j][i] != "X":
                win = False
                break
            else:
                win = True
        if win:
            return win
    return win

#Mark with an X in the table the number given         
def checkTable(table, num):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == num:
                table[i][j] = "X"
    return table

#Read input
with open('Day 4\input1.txt') as f:
    lines = f.readlines()

#Save the numbers order
numOrder = lines[0].split(",")

#Save the tables
tables = []
for i in range(2,len(lines),6):
    table = []
    for j in range(5):
        table.append(lines[i+j].split())
    tables.append(table)

#Check if a table wins following the numbers order
# and save the first winner
winNum = -1
for num in numOrder:
    for tab in range(len(tables)):
        tables[tab] = checkTable(tables[tab], num)
        if checkWin(tables[tab]):
            winNum = num
            winTable = tables[tab]
            break
    if winNum!=-1:
        break

#Calculate the points of the winner table
sum = 0
for i in range(len(winTable)):
    for j in range(len(winTable[0])):
        if winTable[i][j] != "X":
            sum += int(winTable[i][j])

print(int(winNum)*sum)
    