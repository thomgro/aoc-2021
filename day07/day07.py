import AOCUtils
from AOCUtils.fileHandler import *

def calcDistance(array, target):
    distance = 0
    for num in array:
        distance += abs(num - target)
    return distance

def calcComplexDistance(array, target):
    distance = 0
    for num in array:
        steps = abs(num-target)
        if steps > 0:
            for i in range(steps, 0, -1):
                distance += i
    return distance


crabs = openFileAsLineArray("input")[0].split(",")
crabs = [int(x) for x in crabs]

crabs.sort()
max = crabs[-1]

distances = []
for i in range(max+1):
    distances.append(calcDistance(crabs, i))
distances.sort()
print("star 1: %i" % distances[0])

compDistances = []
for i in range(max+1):
    compDistances.append(calcComplexDistance(crabs, i))
compDistances.sort()
print("star 2: %i" % compDistances[0])
