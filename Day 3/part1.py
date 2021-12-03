with open('Day 3\input1.txt') as f:
    lines = f.readlines()

def binaryToDecimal(binary):
     
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal  

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
gamma = binaryToDecimal(int(gamma))
epsilon = binaryToDecimal(int(epsilon))
print(gamma*epsilon)

