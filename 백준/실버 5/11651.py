N = int(input())

X, Y = [], []

M = []

for i in range(N):
    m = list(map(int, input().split()))
    M.append(m)

M.sort(key=lambda x: (x[1], x[0]))

for i in M:
    for j in i:
        print(j, end=' ')
    print("")