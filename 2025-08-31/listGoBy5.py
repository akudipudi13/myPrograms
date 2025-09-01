#ENGLISH#
# I take the amount of values, and I make a list, then I start from the first value and print it, then I count over 5 and 
#pick it up and so on. 

import sys
a = int(input("length of list: "))
if a <= 5:
    print("run again and enter int greater than 5!!! ")
    sys.exit(1)
i = 0
theList = []
while (i < a):
    ele = int(input("Enter int in list "))
    theList.append(ele)
    i = i + 1 
i = 1
while(i < a):
    print(theList[i])
    i = i * 5 


# TEST CASES #
#T1: does the program accuratly print every 5th num?
#length of list: 12
#input: 6, 7, 4, 1, 7, 6, 1, 4, 9, 6, 6, 9
#EO:6,6,6
#PO:

#T2 Does the program exit?
#length of list: 4
#EO: run again and enter proper length , EXIT 



