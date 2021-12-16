import AOCUtils
from AOCUtils.fileHandler import *

fishes = openFileAsLineArray("input.txt")[0].split(",")
fishes = [int(x) for x in fishes]
#fishes = openFileAsLineArray("test.txt")[0].split(",")
#fishes = [int(x) for x in fishes]

for i in range(80):
    spawncount = fishes.count(0)
    fishes = [6 if x == 0 else x-1 for x in fishes]
    fishes.extend([8]*spawncount)

print("star 1: %i" % len(fishes))

listOfLists = []
maxListSize = 700000000

fishes = openFileAsLineArray("input.txt")[0].split(",")
fishes = [int(x) for x in fishes]
listOfLists.append(fishes)

for i in range(256):
    for j in range(len(listOfLists)):
        print(i)
        print(len(listOfLists))
        spawncount = listOfLists[j].count(0)
        listOfLists[j] = [6 if x == 0 else x-1 for x in listOfLists[j]]
        listOfLists[j].extend([8]*spawncount)
        if len(listOfLists[j]) > maxListSize:
            splitIndex = int(len(listOfLists)/2)
            firstHalf = listOfLists[j][:splitIndex]
            secondHalf = listOfLists[j][splitIndex:]
            del listOfLists[j]
            listOfLists.append(firstHalf)
            listOfLists.append(secondHalf)

sum = 0
for list in listOfLists:
    sum += len(list)

print("star2: %i" % sum)