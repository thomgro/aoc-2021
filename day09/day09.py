class HeightElement:
    def __init__(self, height, marked):
        self.height = height
        self.marked = marked

heightMap = []
with open('input') as f:
    for line in f:
        newLine = []
        line = line.rstrip('\n')
        for char in line:
            newLine.append(HeightElement(int(char), False))
        heightMap.append(newLine)
        assert(len(newLine) == 100)
assert(len(heightMap) == 100)
#print(heightMap)

risk = 0
minima=[]
for i in range(100):
    for j in range(100):
        currentHeight = heightMap[i][j].height
        right = False
        down = False
        left = False
        up = False
        if i == 0:
            up = True
        elif currentHeight < heightMap[i-1][j].height:
            up = True 
        if i == 99:
            down = True
        elif currentHeight < heightMap[i+1][j].height:
            down = True
        if j == 0:
            left = True
        elif currentHeight < heightMap[i][j-1].height:
            left = True
        if j == 99:
            right = True
        elif currentHeight < heightMap[i][j+1].height:
            right = True
        if up and right and left and down:
            risk += currentHeight+1
            minima.append([i,j])
print("star 1: %i" % risk)
#print(minima)

def checkNeighbours(i, j):
    if heightMap[i][j].marked or heightMap[i][j].height == 9:
        return 0
    heightMap[i][j].marked = True
    sum = 1
    up = False
    down = False
    left = False
    right = False
    if i != 0 and heightMap[i-1][j].height != 9 and not heightMap[i-1][j].marked:
        up = True
    if i != 99 and heightMap[i+1][j].height != 9 and not heightMap[i+1][j].marked:
        down = True
    if j != 0 and heightMap[i][j-1].height != 9 and not heightMap[i][j-1].marked:
        left = True
    if j != 99 and heightMap[i][j+1].height != 9 and not heightMap[i][j+1].marked:
        right = True
    if up:
        sum += checkNeighbours(i-1, j)
    if down:
        sum += checkNeighbours(i+1, j)
    if left:
        sum += checkNeighbours(i, j-1)
    if right:
        sum += checkNeighbours(i, j+1)
    return int(sum)


basinSizes = []
for coords in minima:
    i, j = coords
    #print(j)
    basinSize = checkNeighbours(i, j)
    basinSizes.append(basinSize)
basinSizes.sort()
#print(basinSizes)
for i in range(100):
    for j in range(100):
        if not heightMap[i][j].marked and heightMap[i][j].height is not 9:
            print(heightMap[i][j].height)
solution2 = basinSizes[-1]*basinSizes[-2]*basinSizes[-3]
assert(len(basinSizes) == len(minima))
print("star 2: %i" % solution2)