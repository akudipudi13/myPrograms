def Findduplicates(listInput):
    for i in range(len(listInput)):
        for x in range(i + 1, len(listInput)):
            if listInput[i] == listInput[x]:
                print(listInput[i])
                break

listInput = input("enter list: ").split()
Findduplicates(listInput)