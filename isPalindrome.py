def checkPalindrome(strInput):
    length = len(strInput)
    for i in range(length%2):
        if strInput[i] != strInput[length - (i + 1)]:
            return False
    return True

strInput = input("String:")
print(checkPalindrome(strInput))