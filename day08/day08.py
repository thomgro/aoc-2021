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