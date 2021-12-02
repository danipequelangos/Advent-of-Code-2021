import re
with open('Day 2\input1.txt') as f:
    lines = f.readlines()

horiz = 0
depth = 0
for i in lines:
    command = (re.sub(r'([a-zA-Z]+)\s[0-9]*',r'\1', i)).rstrip("\n")
    number = int(re.sub(r'[a-zA-Z]+\s([0-9]*)',r'\1', i))
    if command == "forward":
        horiz += number
    elif command == "down":
        depth += number
    elif command == "up":
        depth -= number
    else:
        print("Command not recognized")
print(horiz*depth)