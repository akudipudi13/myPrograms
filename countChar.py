import sys

#char = input("char: ")
#str = input("string: ")
def counting(char, str):
    if len(char) > 1:
        print("only 1 character")
        sys.exit(1)
    charCount = 0
    for i in range(len(str)):
        if str[i] == char:
            charCount += 1
    return charCount
counting('a', 'bAnAna')

