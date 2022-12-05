from collections import defaultdict
from heapq import heappush

lines = [line.strip() for line in open('./inputs/day1.txt', 'r').readlines()]
print(cols)
elfNum = 0
caloriesPerElf = defaultdict(int)
topElves = []

for line in lines:
    if line == "":
        elfNum += 1
        continue
    caloriesPerElf[elfNum] += int(line)

for calories in caloriesPerElf.values():
    heappush(topElves, -calories)

print(-topElves[0])
print(-topElves[0]-topElves[1]-topElves[2])
