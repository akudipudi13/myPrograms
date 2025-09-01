a = int(input("Enter Integer"))
for i in range(a+1):
    if i%2==0:
        print(i)

#TestCases#
## Comprehensive testplan
# Test case 1: Give a number, does the program accurately print even numbers from 0 to input. 
#.    5
#     Expected output: 0,2,4
#.    Program output:  0,2,4
#
# Test case 2: Give a number, does the program accurately print even numbers from 0 to input. 
#     30
#.    Expected output: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
#.    Program output:  0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
#
# Test case 3: Give a number, does the program accurately print even numbers from 0 to input. 
#     100
#     Expected Output: 0 2 4 6 8 10 . . . 100
#     Program output:    0 2 4 6 8 10 . . . 100
#
# 
    
##