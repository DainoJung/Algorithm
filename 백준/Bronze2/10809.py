import string
aList = list(string.ascii_lowercase)

s = str(input())

p = 0

for j in aList:
    if j in s:
        print(s.find(j), end=" ")
    else:
        print(-1, end=" ")
    p += 1
