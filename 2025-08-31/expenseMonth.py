#English#
# Visit each Number    #
#   compare num to the Greatest So Far(gsf)
#   if gsf is bigger, does nothing and moves on 
#   if gsf is smaller the num is now gsf and moves on. 
import sys 
a = int(input("How many months?; "))
if a <= 0:
    print("Run again and enter proper amount of months!")
    sys.exit(1)
sumSoFar = 0
greatestSoFar = -1
for i in range(a):
    b = int(input("How much money on month?; "))
    sumSoFar = b + sumSoFar
    if greatestSoFar < b:
        greatestSoFar = b
total = sumSoFar / a
print(f"Your Average for {a} months is ${total} and your maximum is {greatestSoFar}")

# Test Cases #
# operation: does the program accuratly calculate the average and max?
# months: 3
# money: 10 20 30 30 10 20
# money: 20 30 10 20 30 10
# money: 30 10 20 10 20 30
# EO: Avg: 20, max: 30
# PO: Avg: 20, max: 30

# operation: does the program accuratly stop the program
# months: 0/-1
# EO: enter proper number
# PO: enter proper number

# operation: does the program accuratly calculate the average and max?
# months: 2
# money: 1 2
# money: 2 1
# EO: Avg: 1.5, max: 2
# PO: Avg: 1.5, max: 2


