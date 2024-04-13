N = int(input())

for i in range(N):
    M = str(input())
    s = 0
    p = 0
    for j in M:
        if j == "O":
            p += 1
            s += p
        else:
            p = 0
    print(s)
