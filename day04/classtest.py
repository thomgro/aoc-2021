class myList:
    def __init__(self):
        self.list = []
    
    def addElement(self, element):
        self.list.append(element)
    
    def clearList(self):
        self.list.clear()


listOfLists = []
newList = myList()
for i in range (100):
    if i and not i % 10:
        listOfLists.append(newList)
        newList = myList()    
    newList.addElement(i)
listOfLists.append(newList)

for list in listOfLists:
    print(list.list)
