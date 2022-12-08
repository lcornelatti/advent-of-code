'''
    This day was hard. The code looks bad. No apologies for it.
'''

trees = [line.strip() for line in open('./inputs/day8.txt', 'r').readlines()]

def isVisibleFrom(row, col, dir):

    if row == 0 or row == len(trees) - 1 or col == 0 or col == len(trees[0]) - 1:
        return True
        
    if dir == "R":
        return trees[row][col] > trees[row][col+1] and isVisibleFrom(row, col+1, dir)

    if dir == "L":
        return trees[row][col] > trees[row][col-1] and isVisibleFrom(row, col-1, dir)

    if dir == "U":
        return trees[row][col] > trees[row-1][col] and isVisibleFrom(row-1, col, dir)

    if dir == "D":
        return trees[row][col] > trees[row+1][col] and isVisibleFrom(row+1, col, dir)

def isVisible(row, col):
    return isVisibleFrom(row, col, "U") or isVisibleFrom(row, col, "D") or isVisibleFrom(row, col, "L") or isVisibleFrom(row, col, "R")

numVisible = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        if isVisible(i, j):
            numVisible += 1


def getScore(row, col):

    rightScore = 1
    leftScore = 1
    upScore = 1
    downScore = 1

    if col != len(trees) - 1:
        i = col + 1
        while i < len(trees) - 1:
            print("checking", row, col, i)
            if trees[row][col] > trees[row][i]:
                print(True)
                rightScore += 1
                i += 1
            else:
                print(False)
                break

    if col != 0:
        i = col - 1
        while i >= 1:
            print("checking", row, col, i)
            if trees[row][col] > trees[row][i]:
                print(True)
                leftScore += 1
                i -= 1
            else:
                print(False)
                break

    if row != len(trees) - 1:
        i = row + 1
        while i < len(trees) - 1:
            print("checking", row, col, i)
            if trees[row][col] > trees[i][col]:
                print(True)
                upScore += 1
                i += 1
            else:
                print(False)
                break

    if row != 0:
        i = row - 1
        while i >= 1:
            print("checking", row, col, i)
            if trees[row][col] > trees[i][col]:
                print(True)
                downScore += 1
                i -= 1
            else:
                print(False)
                break

    print(col, row, trees[row][col], upScore, downScore, rightScore, leftScore)
    return upScore * downScore * rightScore * leftScore

maxScore = 0

for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        maxScore = max(getScore(i,j), maxScore)

print(maxScore)