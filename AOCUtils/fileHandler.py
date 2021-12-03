def openFileAsLineArray(path):
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def openFileAsIntArray(path):
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [int(line) for line in lines]
    return lines