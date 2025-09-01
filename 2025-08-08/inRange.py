## English

#  Enters 3 numbers (3, 2, 5) (3rd nummber greater than 2nd number)
#  checks whether 3 is greater than 2. Its is. 
#  then checks whether 3 is less than 5. It is 
#  So if 3 is greater than 2 but less than 5; its in range of 3 and 5. 

#  Assume user gave x  a and b as inputs (assumption : user always gives a smaller than b)
#  if a < x and b > x, x is in the range of a and b
#  in all other cases, its not in the range


a = input("Enter an integer please ") #3
b = input("Enter another integer please ")#2 #4
c = input("Enter another integer please ")#5 #6

if a > b and a< c:  # 3 is greater than 2 but smaller than 5    #3 is less than 4 and 6. 
    print(f"{a} is in the range of {b} and {c}" ) #3 is in the range of 2 and 5 !
else:
    (f"{a} is not in the range of {b} and {c}" ) # 3 is not in the range of 4 and 6


## Comprehensive testplan
# Test case 1: Give a number which is in range, does the program accurately identify that it's in the range
#     3, 2, 5 -- 
#.    Expected output: 
#.    Program output: 
#
# Test case 2: Give a number which is NOT in range(lower than 2 numbers), does the program accurately identify that it's in NOT the range
#     4, 5, 7 
#.    Expected output: 
#.    Program output: 
#
# Test case 3: Give a number which is NOT in range(bigger then 2 numbers), does the program accurately identify that it's in NOT the range
#     9, 5, 7 
#.    Expected output: 
#.    Program output: 
#
# 
