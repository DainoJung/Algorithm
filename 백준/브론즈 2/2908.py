A, B = map(str, input().split())

A1 = int(A[::-1])
B1 = int(B[::-1])

if A1 > B1:
    print(A1)
else:
    print(B1)