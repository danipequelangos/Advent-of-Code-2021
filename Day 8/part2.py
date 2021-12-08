import numpy as np

#Read input
with open('Day 8\input1.txt') as f:
    text = f.readlines()

#Save patterns and digits separetly
patterns = []
digits = []
for i in range(len(text)):
    patterns.append([list(j) for j in (text[i].split("|")[0].split())])
    digits.append([list(j) for j in (text[i].split("|")[1].split())])

def translatePattern(pattern):
    translate = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    #Unique digits
    for i in range(len(pattern)):
        if len(pattern[i]) == 2:
            translate[i] = 1
        elif len(pattern[i]) == 3:
            translate[i] = 7
        elif len(pattern[i]) == 4:
            translate[i] = 4
        elif len(pattern[i]) == 7:
            translate[i] = 8
        if translate.count(-1) == 6:
            break
    #The rest
    for i in [idx for idx, a in enumerate(translate) if a == -1]:
        #Identify 0, 6 and 9
        if len(pattern[i]) == 6:
            count = 0
            #6 intersect 1 == 1 segment
            for j in pattern[translate.index(1)]:
                count += j in pattern[i]
            if count == 1:
                translate[i] = 6
            else:
                count = 0
                #9 intersect 4 == 4 segments
                for j in pattern[translate.index(4)]:
                    count += j in pattern[i]
                if count == 4:
                    translate[i] = 9
                #0 if not 6 neither 9
                else:
                    translate[i] = 0
        #Identify 5, 3 and 2
        if len(pattern[i]) == 5:
            count = 0
            #3 intersect 7 == 2 segments
            for j in pattern[translate.index(7)]:
                count += j in pattern[i]
            if count == 3:
                translate[i] = 3
            else:
                count = 0
                #5 intersect 4 == 3 segments
                for j in pattern[translate.index(4)]:
                    count += j in pattern[i]
                if count == 3:
                    translate[i] = 5
                #2 if not 3 neither 5
                else:
                    translate[i] = 2
    return(translate)

numbers = []
for i in range(len(patterns)):
    translate = translatePattern(patterns[i])
    num = ""
    #Check each digit and add to the number
    for dig in digits[i]:
        for n in range(10):
            if set(patterns[i][n]) == set(dig):
                num += str(translate[n])
                break
    numbers.append(num)
print(sum(list(map(int,numbers))))
