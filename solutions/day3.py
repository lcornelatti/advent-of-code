from collections import defaultdict


def priority(ch):
    if ch.isupper():
        return ord(ch) - ord('A') + 27
    else:
        return ord(ch) - ord('a') + 1


def getPriorityOfCommonItem(line):
    h1, h2 = set(line[:(len(line)//2)]), set(line[(len(line)//2):])
    return priority(h1.intersection(h2).pop())


def getPriorityOfBadge(chunk):
    h1, h2, h3 = set(chunk[0]), set(chunk[1]), set(chunk[2])
    return priority(h1.intersection(h2).intersection(h3).pop())


lines = [line.strip() for line in open('./inputs/day3.txt', 'r').readlines()]
print(sum([getPriorityOfCommonItem(line) for line in lines]))

chunks = [lines[i:i+3] for i in range(0, len(lines), 3)]
print(sum([getPriorityOfBadge(chunk) for chunk in chunks]))
