class CardEntry:
    number = -1
    row = -1
    column = -1
    marked = -1

    def __init__(self, number, row, column):
        self.number = number
        self.row = row
        self.column = column
        self.marked = 0

class BingoCard:
    complete = 0
    entries = []

    def checkCompleteness(self):
        return 0

    def addEntry(self, number, row, column):
        entry = CardEntry(int(number), row, column)
        self.entries.append(entry)
        return 0

    def checkNumber(self, number):
        rowFound = -1
        columnFound = -1
        numberFound = 0
        return [numberFound, rowFound, columnFound]
