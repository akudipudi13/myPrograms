import sys
list1=input("enter list 1: ").split()
list2=input("enter list 2: ").split()
def checkEqualList(list1,list):
    length = len(list1)
    if length != len(list2):
        print("not equal")
        sys.exit(1)
    for i in range(length):
        if list1[i] != list2[i]:
            print("not equal")
            sys.exit(1)
    print("equal")
checkEqualList()