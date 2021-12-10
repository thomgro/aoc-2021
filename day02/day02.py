import AOCUtils
from AOCUtils.fileHandler import *

lines = openFileAsLineArray("input.txt")

horizontal = 0
depth = 0
aim = 0

for line in lines:
    direction = line.split()[0]
    length = int(line.split()[1])

    if direction == "forward":
        horizontal += length
    elif direction == "down":
        depth += length
    elif direction == "up":
        depth -= length
    else:
        print("ERROR: direction not readable: %s" % direction)

magnitude = horizontal*depth
print("star 1: %i" % magnitude)

horizontal = 0
depth = 0

for line in lines:
    direction = line.split()[0]
    length = int(line.split()[1])
    
    if direction == "forward":
        horizontal += length
        depth += length*aim
    elif direction == "down":
        aim += length
    elif direction == "up":
        aim -= length
    else:
        print("ERROR: direction not readable: %s" % direction)

magnitude = horizontal*depth
print("star 2: %i" % magnitude)