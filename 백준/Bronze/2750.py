N = int(input())
S = []

for _ in range(N):
    T = int(input())
    if T in S:
        break
    S.append(T)

S.sort()

for i in S:
    print(i)