import sys

def getCharactercount(char, str):
    
    if len(char) > 1:
        return "only one character!"
    charCount = 0
   
    for i in range(len(str)):
        if str[i] == char:
            charCount += 1
    return charCount

char = input("char: ")
str = input("string: ")

print(getCharactercount(char, str))

