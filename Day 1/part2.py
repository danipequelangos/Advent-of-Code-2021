with open('Day 1\input1.txt') as f:
    lines = f.readlines()

def measurementSums(input):
    sums = []
    for i in range(0,len(input)):
        if i+1 > len(input)-1 or i+2 > len(input)-1:
            break
        else: 
            sums.append(int(input[i])+int(input[i+1])+int(input[i+2]))
    return(sums)

lines = measurementSums(lines)

next = lines[0]
count = 0
for i in lines[1:]:
    if int(i) > int(next):
        count+=1
    next = i
print(count)
