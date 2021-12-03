import AOCUtils
from AOCUtils.fileHandler import *

depths = openFileAsIntArray("first_input")

increaseCount = 0
for i in range(len(depths)-1):
    if depths[i] < depths[i+1]:
        increaseCount += 1

increaseCountThrees = 0
for i in range(len(depths)-3):
    currentWindow = depths[i]+depths[i+1]+depths[i+2]
    nextWindow    = depths[i+1]+depths[i+2]+depths[i+3]
    if currentWindow < nextWindow:
        increaseCountThrees += 1

print("solution 1: number of increases is %i" % increaseCount)
print("solution 2: %i sums are larger than the previous sum" % increaseCountThrees)