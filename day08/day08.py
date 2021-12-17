import AOCUtils
from AOCUtils.fileHandler import *



lines = openFileAsLineArray("input")
inputs = []
outputs = []
for line in lines:
    inputs.append(line.split("|")[0])
    outputs.append(line.split("|")[1])
#print(outputs)

count = 0
uniqueLengths = [2,3,4,7]
for output in outputs:
    digits = output.split()
    for digit in digits:
        if len(digit) in uniqueLengths:
            count += 1

print("star 1: %i" % count)

def findSix(sixSegs, seven):
    #   string, tuple of strings
    for code in sixSegs:
        # when the intersection between the 6-segment-code and the code for 7 is of size 2,
        # we have found the code for the number 6
        if len(set(code) & set(seven)) == 2:
            return code
    print("findSix: this should not happen")
    return '0'

def findUR(six, seven):
    # the UR segment is the one contained in 7 and not in 6
    for char in seven:
        if char not in six:
            return char
    print("findUR: this should not happen")
    return '0'

def findFive(fiveSegs, UR):
    for code in fiveSegs:
        if UR not in code:
            return code
    print("findFive: this should not happen")
    return '0'

#def findThree(fiveSegs)
sum = 0
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
    # we know the numbers 1, 4, 7, 8
    one = twoSegs[0]
    four = fourSegs[0]
    seven = threeSegs[0]
    eight = sevenSegs[0]

    # we can now identify the 6 and remove it from the tuple that contains its code
    six = findSix(sixSegs, seven)
    sixList = list(sixSegs)
    sixList.remove(six)
    sixSegs = tuple(sixList)
    #print(sixSegs)
    
    # now we can identify the upper right (UR) segment and store it:
    UR = findUR(six, seven)
    #print(UR)
    
    # now we can identify the 5 and remove it from the fiveSegs tuple
    five = findFive(fiveSegs, UR)
    fiveList = list(fiveSegs)
    fiveList.remove(five)
    fiveSegs = tuple(fiveList)
    #print(five)
    #print(fiveSegs)
    
    # fiveSegs has two remaining codes, the 3 is the one that shares 4 chars with the code for 5
    # the remaining 5-segment-code has to be number 2
    if len(set(fiveSegs[0]) & set(five)) == 4:
        three = fiveSegs[0]
        two = fiveSegs[1]
    else:
        three = fiveSegs[1]
        two = fiveSegs[0]
    #print(two)
    #print(three)

    # there are two six-segment-codes left, one is for 9, one is for 0
    # the is is that one which contains the entirety of the 5-code (5 segments)
    if len(set(sixSegs[0]) & set(five)) == 5:
        nine = sixSegs[0]
        zero = sixSegs[1]
    else:
        nine = sixSegs[1]
        zero = sixSegs[0]

    digitMap = {
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six: '6',
        seven: '7',
        eight: '8',
        nine: '9',
        zero: '0',
    }
    outCodes = outputs[i].split()
    #print(outCodes)
    number = ''
    for code in outCodes:
        for key in digitMap:
            overlap = len(set(code) & set(key))
            if len(set(code)) == len(set(key)) and len(set(code)) == overlap:
                number += digitMap[key]
    sum += int(number)
    #print(digitMap)
    #print(outCodes)
print("star 2: %i" % sum)