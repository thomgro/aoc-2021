import AOCUtils
from AOCUtils.fileHandler import *
from bingo_card import *

lines = openFileAsLineArray("card.txt")

row = 1
column = 1
card = BingoCard()
for line in lines:
    for x in line.split():
        card.addEntry(x, row, column)
        column += 1
    row += 1
    column = 1

for entry in card.entries:
    print("%i" % entry.number)