
# 6 7 8
# check whether 6 is greater than 7.. 
#     - its lesser. 7 is greatest for now.
#.    - if it's greater, 
# check 7 is greter than 8.. its' lesser.. then 8 is biggest

# Compare first two numbers and dtermine the max
# Compare max & third compare and dtermine the max



user_input_string1 = input("Enter Integer ") # 8
user_input_string2 = input("Enter Integer ") # 7
user_input_string3 = input("Enter Integer ") # 6

user_input_num1 = int(user_input_string1) #user_input_num1 is set to user_input_string1
user_input_num2 = int(user_input_string2)  
user_input_num3 = int(user_input_string3)


# Compare first two numbers and dteermine the greatestSoFar

if user_input_num1 > user_input_num2: # 6 > 7 
    greatestSoFar = user_input_num1
else:
    greatestSoFar = user_input_num2 #  greatestSoFar = 7

# Compare greatestSoFar & third number and dtermine the max
if greatestSoFar > user_input_num3: # 7 > 8
    print(f"{greatestSoFar} is the biggest of the three numbers")
else:
    print(f"{user_input_num3} is the biggest of the three numbers") # 



#if user_input_string1 > user_input_string2:
#    print(user_input_string1 > user_input_string2)
#else:
#    print(user_input_string1 < user_input_string2)

#if user_input_string1 > user_input_string3:
#    print(user_input_string1 > user_input_string3)
#else:
#    print(user_input_string1 < user_input_string3)

#if user_input_string2 > user_input_string3:
#    print(user_input_string2 > user_input_string3)
#else:
#    print(user_input_string2 < user_input_string3)


# Test cases (or test plan)
#  6 7 8: ans is 8
#  8 7 6: ans is 8
#  7 8 6: ans is 8
 


# Homework
# Learn about typecasting
# Practive english solving before attempting code
# mentally testing code without running it

# mentally test cases: 8 7 6 & 7 8 6

# Practice problems
#  - given 3 numbers, print whether the first number is in the range of second and third numbers or not.
#.   Assume 2nd is smaller than 3rd number.
#.   Example: 
#.       3 4 6 -- 3 is in range of 4 6
#.       10 2 8 -- 10 is not in the range of 2 and 8
#  - Given a number, print whether it is a multiple of 3 or not
#.   Examples:
#.       6 - 6 is a multiple of 3
#.       2 - 2 is NOT a multiple of 3 