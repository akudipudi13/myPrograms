 # 5 6 7
# a b c
# check whether 5 is greater than 6.. 
#     - its lesser. 6 is greatest for now. and 5 is the least for now. 
#.    - if it's greater, 
# check 6 is greater than 7.. its' lesser.. then checks if 6 is greater than 5. 6 is greater and 6 is the 2nd biggest. 

# Compare first two numbers then compares greatestSoFar with 3rd number. 
# then compares 3rd number with leastSoFar



a = int(input("Enter Integer ")) # 5
b = int(input("Enter Integer ")) # 6
c = int(input("Enter Integer ")) # 7



# Compare first two numbers and determine the greatestSoFar and leastSoFar

if a > b: # 5 > 6
    greatestSoFar = a
    leastSoFar = b
else:
    greatestSoFar = b
    leastSoFar = a 
# Compare greatestSoFar & third number and third number and leastSoFar to determine the 2nd biggets number
if greatestSoFar > c and c > leastSoFar: 
    print(f"{c} is the 2nd biggest of the three numbers")
if greatestSoFar < c:
    print(f"{greatestSoFar} is the 2nd biggest of the three numbers")
if leastSoFar > c:
    print(f"{leastSoFar} is the 2nd biggest of the 3 numbers")





# Test cases (or test plan)
#  5 6 7: ans is 6
#  7 5 6: ans is 6
#  6 7 5: ans is 6
 

# Step 1: Determine max & secondMax from the first 2 numbers
#maxNum = a
#econdMax = b
#if a < b:
 #  max = b
  # secondMax = a
#
# Step 2: Looking at the 3rd number, determins whether secondmax needs to be updated.
#if c > maxNum:
 #  secondMax = max # 10
#elif c > secondMax:
 #  secondmax = c

#print(secondMax)


