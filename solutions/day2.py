def lineToPointsPart1(line):
    if line in ["A C", "B A", "C B"]:
        return 0
    elif line in ["A B", "B C", "C A"]:
        return 6
    else:
        return 3


def lineToPointsPart2(line):
    if line[2] == "A":
        return (letterToPoints[line[0]] - 1) or 3
    if line[2] == "B":
        return 3 + letterToPoints[line[0]]
    if line[2] == "C":
        return 6 + ((letterToPoints[line[0]] + 1) % 3 or 3)


lines = [line.strip().replace("X", "A").replace(
    "Y", "B").replace("Z", "C") for line in open('./inputs/day2.txt', 'r').readlines()]
letterToPoints = {"A": 1, "B": 2, "C": 3}

print(sum([lineToPointsPart1(line) + letterToPoints[line[2]]
      for line in lines]))
print(sum([lineToPointsPart2(line) for line in lines]))
