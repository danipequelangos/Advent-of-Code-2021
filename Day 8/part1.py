import numpy as np

#Read input
with open('Day 8\input1.txt') as f:
    text = f.readlines()

#Save patterns and digits separetly
patterns = []
digits = []
for i in range(len(text)):
    patterns.append(text[i].split("|")[0].split())
    digits.append(text[i].split("|")[1].split())

count = 0
#Count how many digits of length 2, 3, 4 and 7 are there
for i in range(len(digits)):
    for dig in digits[i]:
        if len(dig) == 2 or len(dig) == 3 or len(dig) == 4 or len(dig) == 7:
            count+=1

print(count)
