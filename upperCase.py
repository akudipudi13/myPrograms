
def convertToUpper(Str):
    upperStr = ""
    for i in range(len(Str)):
        upperStr = upperStr + Str[i].upper()
    return upperStr

print(convertToUpper('Hello'))


