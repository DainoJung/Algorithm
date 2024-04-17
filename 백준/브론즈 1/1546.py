N = int(input())
S = list(map(int, input().split()))

M = max(S)
X = 0

for i in S:
    X += (i / M * 100)

print(X / N)
