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
            newCard.addEntry(x, row, column)
            column += 1
        row += 1
        i += 1
cards.append(newCard)

# read bingo numbers
numberLine = openFileAsLineArray("numbers.txt")
numbers = numberLine[0].split(",")

terminate = 0
winningCard = None
winningNumber = 0
for number in numbers:
    for card in cards:
        found = card.checkNumber(number)
        if found[0]:
            if card.checkCompleteness(found[1], found[2]):
                print("found complete card")
                terminate = 1
                winningCard = card
                winningNumber = number
        if terminate:
            break
    if terminate:
        break

unmarkedSum = 0
for entry in winningCard.entries:
    if not entry.marked:  
        unmarkedSum += int(entry.number)

solution1 = int(unmarkedSum)*int(winningNumber)
print(solution1)