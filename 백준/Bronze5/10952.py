import sys

listSum = []

A, B = 1, 1

while True:
    A, B = map(int, sys.stdin.readline().split())
    if(A == 0 and B == 0):
        break
    sum = A + B
    listSum.append(sum)

for i in listSum:
    print(i)
    