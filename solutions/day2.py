
file1 = open('./inputs/day2.txt', 'r')
lines = file1.readlines()


def part1():
    total = 0
    for count, line in enumerate(lines):

        l = line.strip().split()

        opponent = l[0]
        mymove = l[1]

        outcomePoints = 0
        movepoints = 0
        if opponent == "A":
            if mymove == "X":
                outcomePoints = 3
            elif mymove == "Y":
                outcomePoints = 6
            elif mymove == "Z":
                outcomePoints = 0

        elif opponent == "B":
            if mymove == "X":
                outcomePoints = 0
            elif mymove == "Y":
                outcomePoints = 3
            elif mymove == "Z":
                outcomePoints = 6

        elif opponent == "C":
            if mymove == "X":
                outcomePoints = 6
            elif mymove == "Y":
                outcomePoints = 0
            elif mymove == "Z":
                outcomePoints = 3

        if mymove == "X":
            movepoints = 1
        elif mymove == "Y":
            movepoints = 2
        elif mymove == "Z":
            movepoints = 3
        total += movepoints + outcomePoints

    print(total)


def part2():
    total = 0
    for count, line in enumerate(lines):

        l = line.strip().split()

        opponent = l[0]
        mymove = l[1]

        movepoints = 0
        if opponent == "A":
            if mymove == "X":
                movepoints += 3
            elif mymove == "Y":
                movepoints += 1 + 3
            elif mymove == "Z":
                movepoints += 2 + 6

        elif opponent == "B":
            if mymove == "X":
                movepoints += 1
            elif mymove == "Y":
                movepoints += 2 + 3
            elif mymove == "Z":
                movepoints += 3 + 6

        elif opponent == "C":
            if mymove == "X":
                movepoints += 2
            elif mymove == "Y":
                movepoints += 3 + 3
            elif mymove == "Z":
                movepoints += 1 + 6

        total += movepoints

    print(total)


part1()
part2()
