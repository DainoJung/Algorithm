numList = []

n = 0

for i in range(9):
    numList.append(int(input()))

print(max(numList))

for i in numList:
    n += 1
    if i == max(numList):
        print(n)