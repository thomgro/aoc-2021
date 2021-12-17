import AOCUtils
from AOCUtils.fileHandler import *

lines = openFileAsLineArray("input")
inputs = []
outputs = []
for line in lines:
    inputs.append(line.split("|")[0])
    outputs.append(line.split("|")[1])
print(outputs)

count = 0
uniqueLengths = [2,3,4,7]
for output in outputs:
    digits = output.split()
    for digit in digits:
        if len(digit) in uniqueLengths:
            count += 1

print("star 1: %i" % count)

assert(len(inputs) == len(outputs))
for i in range(len(inputs)):
    digitStrings = inputs[i].split()
    #print(digits)
    twoSegs = tuple([x for x in digitStrings if len(x) == 2])
    threeSegs = tuple([x for x in digitStrings if len(x) == 3])
    fourSegs = tuple([x for x in digitStrings if len(x) == 4])
    fiveSegs = tuple([x for x in digitStrings if len(x) == 5])
    sixSegs = tuple([x for x in digitStrings if len(x) == 6])
    sevenSegs = tuple([x for x in digitStrings if len(x) == 7])
    #print(sevenSegs)
    one = twoSegs[0]
    four = fourSegs[0]
    seven = threeSegs[0]
    eight = sevenSegs[0]
    digitMap = {
        one: '1',
        four: '4',
        seven: '7',
        eight: '8',
    }
    #print(digitMap)
    