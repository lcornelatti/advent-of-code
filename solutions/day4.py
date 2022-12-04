import re


def contains(assignments):
    return (assignments[0] <= assignments[2] and assignments[1] >= assignments[3]) or (
        assignments[2] <= assignments[0] and assignments[3] >= assignments[1])


def overlaps(assignments):
    return not ((assignments[1] < assignments[2]) or (assignments[3] < assignments[0]))


assignments = [list(map(int, re.split('-|,', line.strip())))
               for line in open('./inputs/day4.txt', 'r').readlines()]
print(sum(map(contains, assignments)))
print(sum(map(overlaps, assignments)))
