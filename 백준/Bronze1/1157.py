from string import ascii_uppercase

S = str(input()).capitalize().upper()

aList = list(ascii_uppercase)

bList, cList = [], []

for i in aList:
    bList.append(S.count(i))

for i in range(len(bList)):
    if bList[i] == max(bList):
        cList.append(i)

if len(cList) == 1:
    print(aList[cList[0]])
else:
    print("?")
