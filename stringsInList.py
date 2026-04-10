def listUpperEle(myList):
    length = len(myList)
    theUpperList = [""] * length
    for i in range(length):
        for x in range(len(myList[i])):
            theUpperList[i] += myList[i][x].upper()
    return theUpperList
myList = input("Enter list of strings: ").split()
print(listUpperEle(myList))