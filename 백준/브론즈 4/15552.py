import sys

T = int(input())

listSum = []

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    sum = A + B
    listSum.append(sum)

for i in range(T): 
    print(listSum[i])
    