def nthNum(theList):
    length = len(theList)
    
    for i in range(length//2):
        print(theList[i])
        print(theList[length - (i + 1)])
    
    if length % 2 == 1:
        print(theList[length // 2])

theList = input("enter list: ").split()
nthNum(theList)