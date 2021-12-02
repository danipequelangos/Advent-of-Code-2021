with open('Day 1\input1.txt') as f:
    lines = f.readlines()

next = lines[0]
count = 0
for i in lines[1:]:
    if int(i) > int(next):
        count+=1
    next = i
print(count)
