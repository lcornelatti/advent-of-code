from pprint import pprint
lines = [line.strip() for line in open('./inputs/day7.txt', 'r').readlines()]

def getTotalSizeForDir(d):
    directChildren = sum([int(x[1]) for x in d["fileChildren"]])
    indirectChildren = 0
    for child in d["dirChildren"]:
        indirectChildren += getTotalSizeForDir(fileSystem[child])
    d["totalSize"] = directChildren + indirectChildren
    return d["totalSize"]

dirsInPath = []
fileSystem = {}
lsMode = False
for line in lines:
    if line.startswith("$ cd"):
        dirToMove = line.split(" ")[2]
        if dirToMove == "..":
            dirsInPath.pop()
        else:
            dirsInPath.append(dirToMove)
            fullFilePath = "/".join(dirsInPath)
            fileSystem[fullFilePath] = {"dirChildren": [], "fileChildren": []}
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        fullFilePath = "/".join(dirsInPath)
        fileSystem[fullFilePath]["dirChildren"].append("/".join([fullFilePath, line.split(" ")[1]]))
    else:
        size, fileName = line.split(" ")
        fullFilePath = "/".join(dirsInPath)
        fileSystem[fullFilePath]["fileChildren"].append((fileName, size))

rootSize = getTotalSizeForDir(fileSystem["/"])

# Part 1
s = 0
for val in fileSystem.values():
    if val["totalSize"] <= 100000:
        s += val["totalSize"]
print(s)

# Part 2
freeSpace = 70000000 - rootSize
neededSpace = 30000000 - freeSpace
currentDeletedSize = rootSize
for val in fileSystem.values():
    if val["totalSize"] < currentDeletedSize and val["totalSize"] > neededSpace:
        currentDeletedSize = val["totalSize"]

print(currentDeletedSize)