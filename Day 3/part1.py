with open('Day 3\input1.txt') as f:
    lines = f.readlines()

gamma = ""
epsilon = ""
for bit in range(0, len(lines[0])-1):
    zeros = 0
    ones = 0
    for i in lines:
        if int(i[bit]) == 0:
            zeros+=1
        else:
            ones+=1
    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(gamma, epsilon)
gamma = int(gamma,2)
epsilon = int(epsilon,2)
print(gamma*epsilon)

