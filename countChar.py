import sys

char = input("char: ")
str = input("string: ")
def counting():
    if len(char) > 1:
        print("only 1 character")
        sys.exit(1)
    count = 0
    for i in range(len(str)):
        if str[i] == char:
            count += 1
    print(count)
counting()

