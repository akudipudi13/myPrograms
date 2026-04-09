import sys
def checkEqualList(list1, list2):
    length = len(list1)
    if length != len(list2):
        return False
    for i in range(length):
        if list1[i] != list2[i]:
            return False
    return True
list1=input("enter list 1: ").split()
list2=input("enter list 2: ").split()
if checkEqualList(list1, list2) == True:
    print("equal")
else:
    print("not equal")