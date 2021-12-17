import AOCUtils
from AOCUtils.fileHandler import *

def calcDistance(array, target):
    distance = 0
    for num in array:
        distance += abs(num - target)
    return distance

crabs = openFileAsLineArray("input")[0].split(",")
crabs = [int(x) for x in crabs]

crabs.sort()
min = crabs[0]
max = crabs[-1]

shortestDistance = 999999999
position = -1
distances = []
for i in range(max+1):
    #distance = calcDistance(crabs, i)
    #if distance < shortestDistance:
    #    shortestDistance = distance
    #    position = i
    #print(i)
    #print(distance)
    distances.append(calcDistance(crabs, i))

distances.sort()
print("star 1: %i" % distances[0])