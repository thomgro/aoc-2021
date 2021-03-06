import AOCUtils
from AOCUtils.fileHandler import *

def drawVentDiagonally(coordArray, start, end):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]
    xsign = 0
    ysign = 0
    if x1 < x2:
        xsign = 1
    else:
        xsign = -1
    if y1 < y2:
        ysign = 1
    else:
        ysign = -1
    
    xdistance = abs(x2 - x1)
    ydistance = abs(y2 - y1)
    if xdistance != ydistance:
        print(start)
        print(end)
    xrunner = x1
    yrunner = y1
    while 1:
        coordArray[xrunner][yrunner] += 1
        xrunner += xsign
        yrunner += ysign
        if xrunner == x2:
            coordArray[xrunner][yrunner] += 1
            break

def drawVent(coordArray, vent):
    start = vent[0].split(",")
    end = vent[1].split(",")
    start[0] = int(start[0])
    start[1] = int(start[1])
    end[0] = int(end[0])
    end[1] = int(end[1])
    if start[0] == end[0]:
        runner = start[1]
        # run in positive direction
        if end[1] > start[1]:
            while runner <= end[1]:
                #print("running")
                coordArray[start[0]][runner] += 1
                runner += 1
        # run in negative direction
        elif end[1] < start[1]:
            while runner >= end[1]:
                #print("running")
                coordArray[start[0]][runner] += 1
                runner -= 1
        else:
            "this should not happen"
    elif start[1] == end[1]:
        runner = start[0]
        # run in positive direction
        if end[0] > start[0]:
            while runner <= end[0]:
                #print("running")
                coordArray[runner][start[1]] += 1
                runner += 1
        # run in negative direction
        elif end[0] < start[0]:
            while runner >= end[0]:
                #print("running")
                coordArray[runner][start[1]] += 1
                runner -= 1
        else:
            "this should not happen"
    else:
        drawVentDiagonally(coordArray, start, end)
coordArray = []
for i in range(1000):
    coordArray.append([])
    for j in range(1000):
        coordArray[i].append(0)

lines = openFileAsLineArray("input.txt")
vents = []
for line in lines:
    vents.append(line.split("->"))

for i in range(len(vents)):
    drawVent(coordArray, vents[i])

counter = 0
for i in range(1000):
    for j in range(1000):
        if coordArray[i][j] > 1:
            counter += 1
            #print(coordArray[i][j])
print("star 2: %i" % counter)