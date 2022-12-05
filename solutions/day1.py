from collections import defaultdict
from itertools import groupby, zip_longest
from heapq import heappush

cpe = [sum(map(int, map(lambda x: x.strip(), group)))
       for k, group in groupby(open('./inputs/day1.txt', 'r').readlines(), lambda x: x == "\n") if not k]
print(max(cpe))
print(sum([cpe.pop(cpe.index(max(cpe))) for i in range(3)]))
