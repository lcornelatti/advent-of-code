from itertools import groupby, zip_longest
from copy import deepcopy


def moveMultipleItems(fromStack, toStack, num):
    itemsToMove = fromStack[-num:]
    toStack += itemsToMove
    del fromStack[-num:]


lines = [line.strip() for line in open('./inputs/day5.txt', 'r').readlines()]
startingConfigurations, movements = [
    list(group) for k, group in groupby(lines, lambda x: x == "") if not k]

numColumns = int(startingConfigurations[-1][-1])
columns = list(map(list, zip_longest(*startingConfigurations, fillvalue=" ")))

currentColumn = 0
initialColumnStacks = [[] for i in range(numColumns)]
for col in columns:
    for ch in reversed(col):
        if ch.isalpha():
            initialColumnStacks[currentColumn].append(ch)
        if ch.isnumeric():
            currentColumn = int(ch) - 1

columnStacksPart1 = deepcopy(initialColumnStacks)
[[columnStacksPart1[int(move[5]) - 1].append(columnStacksPart1[int(move[3]) - 1].pop())
  for i in range(int(move[1]))] for move in list(map(lambda x: x.split(), movements))]
print("".join([(col[-1]) for col in columnStacksPart1]))

columnStacksPart2 = deepcopy(initialColumnStacks)
[moveMultipleItems(columnStacksPart2[int(move[3]) - 1], columnStacksPart2[int(move[5]) - 1], int(move[1]))
 for move in list(map(lambda x: x.split(), movements))]
print("".join([(col[-1]) for col in columnStacksPart2]))
