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

population = [fishes.count(0), fishes.count(1), fishes.count(2), fishes.count(3), fishes.count(4), fishes.count(5), fishes.count(6), fishes.count(7), fishes.count(8)]

for i in range(256):
    #print(population)
    spawns = int(population[0])
    for i in range(1,9):
        population[i-1] = population[i]
    population[6] += spawns
    population[8] = spawns

sum = 0
for i in range(len(population)):
    sum += population[i]

print("star 2: %i" % sum)