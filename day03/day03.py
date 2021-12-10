import AOCUtils
from AOCUtils.fileHandler import *

diagnosis = openFileAsLineArray("input.txt")
wordsize = 12

zeros = []
ones = []
gamma = []
epsilon = []

def invert(bit):
    if bit == "1":
        return "0"
    elif bit == "0":
        return "1"
    else:
        print("ERROR: bit %s not recognized" % string(bit))

def binToDec(binWord):
    i = 11
    dec = 0
    for bit in binWord:
        dec += int(bit) * (2**i)
        i -= 1
    return dec

for i in range(wordsize):
    zeros.append(0)
    ones.append(0)
    for line in diagnosis:
        if line[i] == "0":
            zeros[i] += 1
        elif line[i] == "1":
            ones[i] += 1

    if zeros[i] > ones[i]:
        gamma.append("0")
    elif ones[i] > zeros[i]:
        gamma.append("1")
    else:
        print("ERROR: number of 0s and 1s is equal?!")
    
    epsilon.append(invert(gamma[i]))

decGamma = binToDec(gamma)
decEpsilon = binToDec(epsilon)

powerConsumption = decGamma * decEpsilon
print("star 1: %i" % powerConsumption)

#oxygen
oxygenDiagnosis = openFileAsLineArray("input.txt")
for i in range(wordsize):
    ones = 0
    zeros = 0
    for line in oxygenDiagnosis:
        if line[i] == "0":
            zeros += 1
        elif line[i] == "1":
            ones += 1
    
    if ones >= zeros:
        oxygenDiagnosis = [x for x in oxygenDiagnosis if x[i] == "1"] 
    else:
        oxygenDiagnosis = [x for x in oxygenDiagnosis if x[i] == "0"]
    
    if len(oxygenDiagnosis) == 1:
        break

#co2
co2Diagnosis = openFileAsLineArray("input.txt")
for i in range(wordsize):
    ones = 0
    zeros = 0
    for line in co2Diagnosis:
        if line[i] == "0":
            zeros += 1
        elif line[i] == "1":
            ones += 1
    
    if ones >= zeros:
        co2Diagnosis = [x for x in co2Diagnosis if x[i] == "0"] 
    else:
        co2Diagnosis = [x for x in co2Diagnosis if x[i] == "1"]
    
    if len(co2Diagnosis) == 1:
        break

oxy = binToDec(oxygenDiagnosis[0])
co2 = binToDec(co2Diagnosis[0])
result = oxy*co2

print("star 2: %i" % result)