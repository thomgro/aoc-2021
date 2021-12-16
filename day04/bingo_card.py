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
    def __init__(self):
        self.entries = []

    def checkCompleteness(self, row, column):
        rowCount = 0
        columnCount = 0
        for entry in self.entries:
            if entry.row == row and entry.marked:
                rowCount += 1
            if entry.column == column and entry.marked:
                columnCount += 1
        if rowCount == 5 or columnCount == 5:
            return 1
        else:
            return 0

    def addEntry(self, number, row, column):
        entry = CardEntry(int(number), row, column)
        self.entries.append(entry)
        return 0

    def checkNumber(self, number):
        rowFound = -1
        columnFound = -1
        numberFound = 0
        for i in range (len(self.entries)):
            if int(self.entries[i].number) == int(number):
                rowFound = self.entries[i].row
                columnFound = self.entries[i].column
                self.entries[i].marked = 1
                numberFound = 1
                return [numberFound, rowFound, columnFound]
        return [numberFound, rowFound, columnFound]
    
    def unmarkedSum(self):
        sum = 0
        for entry in self.entries:
            if not entry.marked:
                sum += entry.number
        return sum
