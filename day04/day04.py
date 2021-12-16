import AOCUtils
from AOCUtils.fileHandler import *
from bingo_card import *

# read bingo cards
lines = openFileAsLineArray("input.txt")
row = 1
column = 1
cards = []
i = 0
newCard = BingoCard()
row = 1
column = 1
for line in lines:
    if line:
        # every 5th non-empty line after the first 5 is a new card
        if i % 5 == 0 and i > 0:
            cards.append(newCard)
            newCard = BingoCard()
            row = 1
        column = 1    
        for x in line.split():
            newCard.addEntry(x, row, column, 0)
            column += 1
        row += 1
        i += 1
cards.append(newCard)

def copyCard(card):
    newCard = BingoCard()
    for entry in card.entries:
        newCard.addEntry(entry.number, entry.row, entry.column, entry.marked)
    return newCard

# read bingo numbers
numberLine = openFileAsLineArray("numbers.txt")
numbers = numberLine[0].split(",")

terminate = 0
firstWinningCard = None
firstWinningNumber = 0
lastWinningCard = None
lastWinningNumber = 0
for number in numbers:
    for card in cards:
        found = card.checkNumber(number)
        if found[0]:
            if card.checkCompleteness(found[1], found[2]):
                if not terminate:
                    firstWinningCard = copyCard(card)
                    firstWinningNumber = int(number)
                    terminate = 1
                elif not card.won:
                    lastWinningCard = copyCard(card)
                    lastWinningNumber = int(number)
                    card.won = 1

unmarkedSum = 0
for entry in firstWinningCard.entries:
    if not entry.marked:  
        unmarkedSum += int(entry.number)
solution1 = int(unmarkedSum)*int(firstWinningNumber)
print("star 1: %i" % solution1)

unmarkedSum = 0
for entry in lastWinningCard.entries:
    if not entry.marked:
        unmarkedSum += int(entry.number)
solution2 = int(unmarkedSum)*int(lastWinningNumber)
print("star 2: %i" % solution2)