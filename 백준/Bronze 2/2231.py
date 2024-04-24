N = int(input())

S = []

for j in range(1, N + 1):
    k = j
    for i in str(j):
        k += int(i)
    if k == N:
        S.append(j)
        break

if len(S) != 0:
    print(S[0])
else:
    print(0)