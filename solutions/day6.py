message = open('./inputs/day6.txt', 'r').readline()

def printIndexAfterNDistinct(n):
    print(list(filter(lambda i: len(set(message[i: i+n])) == n, [i for i in range(len(message))]))[0]+n)

printIndexAfterNDistinct(4)
printIndexAfterNDistinct(14)