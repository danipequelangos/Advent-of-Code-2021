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

oxygen = lines
for bit in range(0, len(oxygen[0])-1):
    zeros = []
    ones = []
    if(len(oxygen)>1):
        for i in oxygen:
            if int(i[bit]) == 0:
                zeros.append(i)
            else:
                ones.append(i)
    else:
        break
    if len(ones) >= len(zeros):
        oxygen = ones
    else:
        oxygen = zeros

CO2=lines
for bit in range(0, len(CO2[0])-1):
    zeros = []
    ones = []
    if(len(CO2)>1):
        for i in CO2:
            if int(i[bit]) == 0:
                zeros.append(i)
            else:
                ones.append(i)
    else:
        break
    if len(zeros) <= len(ones):
        CO2 = zeros
    else:
        CO2 = ones

print(binaryToDecimal(int(oxygen[0]))*binaryToDecimal(int(CO2[0])))

