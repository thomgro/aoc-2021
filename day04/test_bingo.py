import pytest
import AOCUtils
from AOCUtils.fileHandler import *
from bingo_card import *

@pytest.fixture
def card():
    lines = openFileAsLineArray("card.txt")
    row = 1
    column = 1
    card = BingoCard()
    card.entries.clear()
    for line in lines:
        for x in line.split():
            card.addEntry(x, row, column)
            column += 1
        row += 1
        column = 1
    return card

# Bingo card should look like this:
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
 
def test_entryPosition(card):
    for entry in card.entries:
        if entry.number == 23:
            assert entry.row == 2
            assert entry.column == 3
        if entry.number == 19:
            assert entry.row == 5
            assert entry.column == 5

def test_marking(card):
    # bool, row, column
    assert len(card.entries) == 25
    checkList = card.checkNumber(2)
    assert checkList[0] == 1
    
    for entry in card.entries:
        if entry.number == 2:
            assert entry.marked == 1
        else:
            assert entry.marked == 0

def test_complete(card):
    assert len(card.entries) == 25
    assert card.unmarkedSum() == 300
    card.checkNumber(21)
    card.checkNumber(10)
    card.checkNumber(14)
    card.checkNumber(9)
    card.checkNumber(16)
    card.checkNumber(7)
    assert card.checkCompleteness(3, 5)
    assert card.checkCompleteness(4, 1) == 0
    assert card.unmarkedSum() == 223

def test_inputCards():
    lines = openFileAsLineArray("input.txt")
    cards = []
    i = 0
    newCard = BingoCard()
    for line in lines:
        row = 1
        column = 1
        if line:
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
    assert len(cards) == 100
    for card in cards:
        assert len(card.entries) == 25