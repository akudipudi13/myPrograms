# ENGLISH #
# So num is 5 and I guess 20, so then I will check, is 20 greater, less, or equal to num(5) ? its greater, so then 
#it will guess 3, and I will check is 3 greater, less than, or equal to 5? its less than. So it will guess 5, is 5 greater,
#less than, or equal to 5? equal to! BINGO!!!
import random
import sys 
print("Guess a number between 0 - 100000.")
a = int(input("What's your guess?; "))
num = random.randint(0, 100000)

i = 0

while(i == 0):
    if a == num:
        print("BINGO!")
        sys.exit(0)
    elif a < num:
        a = int(input("The number is BIGGER!, guess again; "))
    elif a > num:
        a = int(input("The number is SMALLER!, guess again; "))

# Test Cases #
# operation: does the program correctly say 
#how it compares to each number guess
# int: 5
# input: 6, 4, 5 
# EO: 6: my num is smaller 4: my num is bigger
#5: bingo
# PO: 6: my num is smaller 4: my num is bigger
#5: bingo

# operation: does the program correctly say how 
#it compares to each number guess
# int: 0
# input: -1, 1, 0
# EO: 1: my num is smaller -1: my num is bigger
#0: bingo
# PO: 1: my num is smaller -1: my num is bigger
#0: bingo

