#English#
# Ask Input
# create lower case version
# create upper case version
# check if og string = uppercase version
#   print uppercase
# else if og string = lower case version
#   print lowercase
#else
#   print mixedcase

str = str(input('String: '))
upper = str.upper()
lower = str.lower()
if str == upper:
    print('uppercase')
elif str == lower:
    print('lowercase')
else:
    print('mixed case')

#Test Cases#
#"HELLO"
#uppercase

#'hello'
#lowercase

#Hello
#mixed case