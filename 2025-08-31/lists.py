a = int(input("Enter integer 1  "))
b = int(input("Enter integer 2  "))
c = int(input("Enter integer 3  "))
d = int(input("Enter integer 4  "))
my_list = [a, b, c, d]
#print("Inital list:")
#print(my_list)
#my_list += [3]
#print("After addition:")
#print(my_list)
#my_list.remove(4)
#print("After removal:")
#print(my_list)

print("Printing length of lists:")
print(len(my_list))

print("Printing element by traversing manually:")
for i in range(len(my_list)):
    print(my_list[i])