import sys

listSum = []

A, B = 1, 1

count = 0

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break