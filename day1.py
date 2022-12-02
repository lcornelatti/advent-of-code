file1 = open('./inputs/day1.txt', 'r')
lines = file1.readlines()

elfNum = 0
newElf = True
caloriesPerElf = {}
for count, line in enumerate(lines):

    l = line.strip()

    if l == "":
        newElf = True
        elfNum += 1
        continue

    if newElf:
        caloriesPerElf[elfNum] = int(l)
        newElf = False
    else:
        caloriesPerElf[elfNum] += int(l)

c1 = 0
c2 = 0
c3 = 0

for elf, calories in caloriesPerElf.items():
    if calories > c1:
        c3 = c2
        c2 = c1
        c1 = calories
    elif calories > c2:
        c3 = c2
        c2 = calories
    elif calories > c3:
        c3 = calories

print(c1)
print(c1+c2+c3)
