moves = [(line.strip().split()[0], int(line.strip().split()[1])) for line in open('./inputs/day9.txt', 'r').readlines()]

knotPos = [(0,0) for _ in range(10)]
visited = [set([(0,0)]) for _ in range(10)]

def getNewHPos(hPos, direction):
    if direction == "R":
        return (hPos[0], hPos[1]+1)
    elif direction == "L":
        return (hPos[0], hPos[1]-1)
    elif direction == "U":
        return (hPos[0]-1, hPos[1])
    elif direction == "D":
        return (hPos[0]+1, hPos[1])

def getNewTPos(hPos, tPos, i):
    if abs(hPos[0] - tPos[0]) < 2 and abs(hPos[1] - tPos[1]) < 2:
        return tPos
    newX, newY = tPos[0], tPos[1]
    if hPos[0] > tPos[0] :
        newX = tPos[0] + 1
    if hPos[0] < tPos[0] :
        newX = tPos[0] -1
    if hPos[1] > tPos[1] :
        newY = tPos[1] + 1
    if hPos[1] < tPos[1] :
        newY = tPos[1] -1
    return (newX, newY)

for direction, numSteps in moves:
    for step in range(numSteps):
        knotPos[0] = getNewHPos(knotPos[0], direction)
        for i in range(1, 10):
            knotPos[i] = getNewTPos(knotPos[i-1], knotPos[i], i)
            visited[i].add(knotPos[i])

print(len(visited[1]), len(visited[-1]))
