## English 
#  checks if a is divisible by 3. 
#  if a is divisble by 3, it is an multiple of 3
#  if a is not divisble by 3, it is not an multiple by 3 

a = input("Enter an Integer Please ")  #9 #7
if (a % 3) == 0:                       #9%3=0r  #7%3=1r
    print(f"{a} is a multiple of 3! ") # 9 is a multiple of 3!
else:
    print(f"{a} is NOT a multiple of 3. ") # 7 is NOT a multiple of 3

    ## test cases !! 
    # Test case 1: Goiven a 3 multiple, does the program accurately say its' a 3 multiple
    #. 9
    #. Expected output: 9 is a multiple of 3/divisible by 3
    #. Program output: 9 is a multiple of 3!
    #
    # Test case 2: Goiven a non 3 multiple, does the program accurately say its' a NOT 3 multiple
    #. 2
    #. Expected output: 2 isn't a multiple of 3/not divisible by 3
    #. Program output: 2 is NOT a multiple of 3

    
    
    