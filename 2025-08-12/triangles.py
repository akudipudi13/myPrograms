#checks if a is equal to b and c. 
# if true; its equilateral
#checks if a is equal to b but not c 
# if true; its isosceles
#checks if a is equal to c but not b
# if true; its isosceles
#checks if a is not equal to b and c is not equal to b 
# if true; its scalene 




a = int(input("Enter the length of on side on your triangle "))
b = int(input("Enter the length of another side on your triangle "))
c = int(input("Enter the length of the last side on your triangle "))

if a == b and b == c: 
    print("Your triangle is equilateral!")
elif a == b and b != c:
    print("Your triangle is isosceles!")
elif a == c and c != b:
    print("Your triangle is isosceles!")
elif a != c and c == b:
    print("Your triangle is isosceles!")
if a != c and a != b:
    print("Your triangle is scalene!")

    #testcases: 
    #   1, 1, 1
    #   2, 2, 3
    #   2, 3, 2
    #   1, 2, 3


    # 2 3 3

    #if a == b:
     #   # equilatetal
      ## else:
            # isoceles
        #    print("Your triangle is isosceles!")
    #elif b == c:
        # isoceles
     #   print("Your triangle is isosceles!")
    #else:
     #   print("Your triangle is scalene!")
