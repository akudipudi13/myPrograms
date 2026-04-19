def checkPali(String):
    length = len(String)
    for i in range(length%2):
        if String[i] != String[length - (i + 1)]:
            return False
    return True

String = input("String: ")